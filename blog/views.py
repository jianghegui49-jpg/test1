from django.shortcuts import render
import datetime

def home(request):
    context = {'now': datetime.datetime.now()}
    return render(request, 'home.html', context)