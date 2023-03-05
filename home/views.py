from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
import openai
import os
from dotenv import load_dotenv
import dotenv

# Create your views here.

TEMPLATE_DIRS = ('home/templates',)

# def index(request):   
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input', '')
#         if user_input.strip():
#             openai.api_key = os.getenv("OPENAI_API_KEY")
#             msgs = []
#             msgs.append({"role": "system", "content": "What type of chatbot would you like to create?"})
#             msgs.append({"role": "user", "content": user_input})
#             response = openai.Completion.create(
#                 engine="text-davinci-002",
#                 prompt="Conversation with AI:\n\nUser: {}\nAI:".format(user_input),
#                 max_tokens=60,
#                 n=1,
#                 stop=None,
#                 temperature=0.7,
#             )
#             ai_response = response.choices[0].text.strip()
#             msgs.append({"role": "assistant", "content": ai_response})
#             #return JsonResponse({'data': ai_response})     
#             return render(request,"index.html",{"data":ai_response})
#     return render(request,"index.html",{"data":"Hello World1"})

def index(request):   
    if request.method == 'POST':
        load_dotenv() # Load all the ENV variables into your os enviroment.
        user_input = request.POST.get('user_input', '')
        if user_input.strip():
            msg = user_input
            openai.api_key = os.getenv("OPENAI_API_KEY")
            msgs = []
            msgs.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs)
            reply = response["choices"][0]["message"]["content"]
            msgs.append ({"role": "user", "content": msg})
            #return JsonResponse({'data': ai_response})     
            msgs.append({"role": "assistant", "content": reply})
            return render(request,"index.html",{"data":reply,"data2":response})
    return render(request,"index.html",{"data":"Hello World1"})


# load_dotenv() # Load all the ENV variables into your os enviroment.
# openai.api_key = os.getenv("OPENAI_API_KEY") # Get your API key from an environment variable
# msgs = []
# system_msg = input("What type of chatbot would you like to create?\n")
# msgs.append ({"role": "system", "content": system_msg})
# print("Say hello to your new chatbot! Type quit() when done.")
# while True:
#   msg = input("YOU: ")
#   if "quit()" in msg:
#    break
#   msgs.append ({"role": "user", "content": msg})
#   response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs)
#   reply = response["choices"][0]["message"]["content"]
#   msgs.append({"role": "assistant", "content": reply})
#   print("\nAI: " + reply + "\n")