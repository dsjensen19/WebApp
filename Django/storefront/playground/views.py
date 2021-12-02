from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request, 'Home.html', {'name': 'Derek'})

def find(request):
    return render(request, 'BoardGameFinder.html')

def group(request):
    return render(request, 'GroupFinder.html')
