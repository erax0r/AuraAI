# gpt 3
import os
import openai
from dotenv import load_dotenv
import dotenv
load_dotenv() # Load all the ENV variables into your os enviroment.
openai.api_key = os.getenv("OPENAI_API_KEY") # Get your API key from an environment variable
msgs = []
system_msg = input("What type of chatbot would you like to create?\n")
msgs.append ({"role": "system", "content": system_msg})
print("Say hello to your new chatbot! Type quit() when done.")
while True:
  msg = input("YOU: ")
  if "quit()" in msg:
   break
  msgs.append ({"role": "user", "content": msg})
  response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs)
  reply = response["choices"][0]["message"]["content"]
  msgs.append({"role": "assistant", "content": reply})
  print("\nAI: " + reply + "\n")
  