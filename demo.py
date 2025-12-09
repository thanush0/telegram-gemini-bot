import google.generativeai as genai

genai.configure(api_key="AIzaSyCF6wmhVMyC5_c8gGsLr1Z3Ya1xQ6nbSnM")

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Hello")
print(response.text)
