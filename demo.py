import google.generativeai as genai

genai.configure(api_key="REDACTED_BY_GEMINI_CLI")

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Hello")
print(response.text)
