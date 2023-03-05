from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
import openai
import os
from dotenv import load_dotenv
import dotenv

# Create your views here.

TEMPLATE_DIRS = ('home/templates',)

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
