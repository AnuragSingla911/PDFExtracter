


import sys



import io

import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path):
    # Convert PDF to image
    pages = convert_from_path(pdf_path, 500)
     
    # Extract text from each page using Tesseract OCR
    text_data = ''
    for page in pages:
        text = pytesseract.image_to_string(page)
        text_data += text + '\n'
     
    # Return the text data
    return text_data
 
text = extract_text_from_pdf('RenewalPremium_26709508.pdf')
print(len(text))


import os
import wandb
from openai import OpenAI
client = OpenAI(api_key='sk-abc');

# Define a paragraph to be summarized
paragraph = text

# Create a prompt for summarization
prompt = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f"Extract policy number, receipt number, premium amount from below text : '{paragraph}'"},
]




temperature=0.2
max_tokens=256
frequency_penalty=0.0


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    frequency_penalty=frequency_penalty
)
print(response.choices[0].message.content)

