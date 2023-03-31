import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_completion(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message
