from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
import openai
import os

# Create your views here.

TEMPLATE_DIRS = ('home/templates',)

def index(request):   
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        if user_input.strip():
            openai.api_key = os.getenv("OPENAI_API_KEY")
            msgs = []
            msgs.append({"role": "system", "content": "What type of chatbot would you like to create?"})
            msgs.append({"role": "user", "content": user_input})
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt="Conversation with AI:\n\nUser: {}\nAI:".format(user_input),
                max_tokens=60,
                n=1,
                stop=None,
                temperature=0.7,
            )
            ai_response = response.choices[0].text.strip()
            msgs.append({"role": "assistant", "content": ai_response})
            #return JsonResponse({'data': ai_response})     
            return render(request,"index.html",{"data":ai_response})
    return render(request,"index.html",{"data":"Hello World1"})