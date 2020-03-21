from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request , 'learning_logs/index.html' ,{'new_learning_log_text':request.POST.get('learning_log_text', ''),})

