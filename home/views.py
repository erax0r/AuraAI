from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
import openai
import os
from dotenv import load_dotenv
import dotenv
import json

# Create your views here.

TEMPLATE_DIRS = ('home/templates',)

# def index(request):   
#     if request.method == 'POST':
#         load_dotenv() # Load all the ENV variables into your os enviroment.
#         user_input = request.POST.get('user_input', '')
#         hidden_input = request.POST.get('my_hidden_input', '')
#         if user_input.strip():
#             msg = user_input
#             history = hidden_input
#             openai.api_key = os.getenv("OPENAI_API_KEY")
#             msgs = []
#             # msgs.append(hidden_input)
#             msgs.append({"role": "user", "content": user_input})
#             response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs)
#             reply = response["choices"][0]["message"]["content"]
#             #  msgs.append ({"role": "user", "content": msg})
#             #return JsonResponse({'data': ai_response})     
#             msgs.append({"role": "assistant", "content": reply})
#             return render(request,"index.html",{"data":reply,"data2":msgs})
#     return render(request,"index.html",{"data":"Hello World1"})

def index(request):
    if request.method == 'POST':
        load_dotenv() # Load all the ENV variables into your os enviroment.
        user_input = request.POST.get('user_input', '')
        hidden_input = request.POST.get('my_hidden_input', '')
        if user_input.strip():
            msgs = []
            if hidden_input.strip():
                # Convert the hidden_input string to a Python object
                history = json.loads(hidden_input)                
                # Append the history to the msgs list
                # is there a better way to do this, its slow and inefficient, does not scale
                for msg in history:
                    msgs.append(msg)
            # Append the user input to the msgs list
            msgs.append({"role": "user", "content": user_input})
            openai.api_key = os.getenv("OPENAI_API_KEY")
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs)
            reply = response["choices"][0]["message"]["content"]
            # Append the AI response to the msgs list
            msgs.append({"role": "assistant", "content": reply})
            # Convert the msgs list to a JSON string
            msgs_json = json.dumps(msgs)
            return render(request, "index.html", {"data": reply, "data2": msgs_json})
    return render(request, "index.html", {"data": ""})