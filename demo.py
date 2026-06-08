import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

try:
    response = model.generate_content("Hello")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
