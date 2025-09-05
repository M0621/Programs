from google import genai
import random

#Simple gemini chat bot

client = genai.Client(api_key='')  #Not in code for privacy reasons as this repository is public, but will be when code is being used
chat = client.chats.create(model="gemini-2.0-flash")

while True:
    message = input(">")
    if message == "exit":
        break

    res = chat.send_message(message)
    print(res.text)
