# read text file
with open("text_sample.txt", "r", encoding="utf-8") as file:
    contents = file.read()

import re
import string
import unicodedata
import ftfy
import nltk
from nltk.corpus import stopwords
from spellchecker import SpellChecker

# spacing and lowercase
no_space = re.sub(r' +', ' ', contents).strip().lower()

# remove punctuation
no_punct = no_space.translate(str.maketrans('', '', string.punctuation))

# remove emojis
emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "\U00002700-\U000027BF"
    "\U0001F900-\U0001F9FF"
    "\U00002600-\U000026FF"
    "\U00002B50-\U00002B55"
    "]+", flags=re.UNICODE
)
clean_text_no_emoji = emoji_pattern.sub('', no_punct)

# encoding issues
fixed_text = ftfy.fix_text(clean_text_no_emoji)
normalized_text = unicodedata.normalize('NFKD', fixed_text).encode('ascii', 'ignore').decode()

# remove numbers
no_numbers = re.sub(r'\d+', '', normalized_text)

# remove stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

no_stopwords = remove_stopwords(no_numbers)

# remove HTML tags
def remove_html_tags(text):
    return re.sub(r'<[^>]+>', '', text)

no_html = remove_html_tags(no_stopwords)

# correct typos
spell = SpellChecker()

def correct_typos(text):
    words = text.split()
    corrected_words = []
    for word in words:
        if word in spell or len(word) <= 3:  
            corrected_words.append(word)
        else:
            correction = spell.correction(word)
            corrected_words.append(correction if correction else word)
    return " ".join(corrected_words)

final_clean_text = correct_typos(no_html)

# result
with open("cleaned_output.txt", "w", encoding="utf-8") as file:
    file.write(final_clean_text)
