import requests
import pdfplumber
from dotenv import load_dotenv
import os

load_dotenv()

with pdfplumber.open("RuchilPatel_Resume.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)


text = text

endpoint = 'https://api.murf.ai/v1/speech/generate'

headers = {
    'api-key': os.getenv("API_KEY")
}

params = {
    'text': text,
    "voiceId": "en-US-ken"
}

response = requests.post(url=endpoint, headers=headers, json=params)

speech = response.json()

print(speech['audioFile'])

