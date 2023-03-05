import os
import openai
from dotenv import load_dotenv
import dotenv


#get input from user and send to openai
def getResponse(msg): 
    # load_dotenv() # Load all the ENV variables into your os enviroment.
    # openai.api_key = os.getenv("OPENAI_API_KEY") # Get your API key from an environment variable
    openai.api_key = "test"
    msgs = []
    system_msg = "test"
    msgs.append ({"role": "system", "content": system_msg})
    msgs.append ({"role": "user", "content": msg})
   
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs)
    reply = response["choices"][0]["message"]["content"]
    msgs.append({"role": "assistant", "content": reply})
    
    # print("\nAI: " + reply + "\n")
    return reply
