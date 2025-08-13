import re

text = """
Name: John Smith
Email: john.smi@example.com
Phone: +1 (416) 555-1234
LoanID: L-2025-0042
Date of Birth: 2000-08-15
Address: 456 Hudson St, Jersey City, NJ 07302
"""

match = re.search("LoanID", text)

if match:
  print(match)

#Extract email
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)
print("Emails:", emails)

# Extract phone numbers
phones = re.findall(r"\+?\d[\d\s().-]{9,}", text)
print("Phones:", phones)

# Extract dates (YYYY-MM-DD)
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
print("Dates:", dates)


#how to draw visual bounding box for checking purposes
import cv2
import numpy as np
from PIL import Image

# Convert PDF page to an image
pix = doc[0].get_pixmap()
img = np.array(Image.frombytes("RGB", [pix.width, pix.height], pix.samples))

# Convert image to OpenCV BGR format
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Get the actual image height
img_height = img.shape[0]  # OpenCV uses (height, width, channels)

# Extract words and their bounding boxes
words = doc[0].get_text("words")

# Define the field we are looking for
target_word = "123-456-7890"  # Replace with actual phone number

# Flag to check if the word was found
word_found = False

# Search for the target word and retrieve its bounding box
for word in words:
x0, y0, x1, y1, text, block, line, word_no = word  # Unpack correctly

if target_word in text:  # Case-sensitive match (modify if needed)
# Convert PyMuPDF's y-coordinates (bottom-left origin) to OpenCV's (top-left origin)
y0_new = y1  # Convert bottom-left to top-left
y1_new = y0  # Convert bottom-left to top-left

# Convert coordinates to integers
x0, y0_new, x1, y1_new = map(int, [x0, y0_new, x1, y1_new])

# Draw a rectangle around the detected word
cv2.rectangle(img, (x0, y0_new), (x1, y1_new), (0, 255, 0), 2)

print(f"Found '{target_word}' at: ({x0}, {y0_new}, {x1}, {y1_new})")
word_found = True

# Ensure an image is displayed even if no word is found
if not word_found:
print(f"'{target_word}' not found in document.")

# Convert back to RGB for displaying in PIL
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image using PIL (works in Jupyter/Colab)
display(Image.fromarray(img_rgb))



#how to use anchors with coordinates

words = doc[0].get_text("words")  # Get all words with their positions

for word in words:
    x0, y0, x1, y1, w_text, *_ = word
    if "123-456-7890" in w_text:
        print(f"Found phone number at: ({x0}, {y0}, {x1}, {y1})")

    if "Contact Info" in w_text:
        print(f"Found anchor phrase at: ({x0}, {y0}, {x1}, {y1})")




#locate what u found

words = doc[0].get_text("words")

target_word = phone_number

for word in words:
    x0, y0, x1, y1, text, block, line, word_no = word
    if target_word.lower() in text.lower():
        print(f"Found '{target_word}' at: ({x0}, {y0}, {x1}, {y1})")
