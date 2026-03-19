#Chatbot using Gemini API
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyBzgUdwmaA9wfhQfS4DipQI0nr0CubKMbc")

def get_response(prompt):
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt
    )
    return(response.text)

# prompt=input("Enter the question: ")
# print(get_response(prompt))
