import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# List available models
try:
    models = genai.list_models()
    for m in models:
        print(f"Model: {m.name}")
except Exception as e:
    print(f"Error listing models: {e}")
