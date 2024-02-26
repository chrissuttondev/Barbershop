
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home(request):

    template_name = "home/index.html"
    
    return render(
        request,
        'home/index.html')