!pip install pymupdf

from google.colab import files
uploaded = files.upload()

#code by Shriya Kalyan

import fitz

doc = fitz.open("LenderFeesWorksheetNew.pdf")
print(f"Total pages: {doc.page_count}")
print("PDF Metadata")
doc.metadata

page = doc[0]
text = page.get_text("words")
#print(text)

structured_output = []

for item in text:
  word = item[4]
  bbox = item[0:4]

  structured_output.append({
      "text" : word,
      "bbox" : bbox
  })

print(structured_output)

import json

with open("structured_output.json", "w") as file:
    json.dump(structured_output, file, indent=2)
