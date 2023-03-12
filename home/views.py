from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
import openai
import os
from dotenv import load_dotenv
import dotenv
import json
import datetime

# Create your views here.

TEMPLATE_DIRS = ('home/templates',)

def index(request):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if request.method == 'POST':
        load_dotenv() # Load all the ENV variables into your os enviroment.
        user_input = request.POST.get('user_input', '')
        hidden_input = request.POST.get('conversation', '')
        if user_input.strip():            
            if hidden_input:
                conversation = json.loads(hidden_input)                
            else:
                conversation = []
            conversation.append({"role": "user", "content": user_input})
            openai.api_key = os.getenv("OPENAI_API_KEY")
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation,user="test123")
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            reply = response["choices"][0]["message"]["content"].lstrip()
            conversation.append({"role": "assistant", "content": reply})
            logRequest(request,conversation) #log the conversation
            msgsjson = json.dumps(conversation)            
            return render(request, "index.html", {"data": reply, "data2": conversation, "data3": msgsjson})
    return render(request, "index.html", {"data": ""})

def logRequest(request,msgs):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    user_ip = request.META.get('REMOTE_ADDR', '') # Get the user's IP address
    log_file_path = f'logs/{user_ip}.txt' # Set the path and name of the log file
    if request.method == 'POST':
        # rest of your code
        msgs_json = json.dumps(msgs)
        
        # Create the logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        # Append or create the log file
        with open(log_file_path, 'a+') as f:
            f.write(msgs_json + '\n')
        # rest of your code
    return
