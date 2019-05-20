from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render (request, 'MediumEdit/med_edit_test.html')

def about(request):
    return HttpResponse('<h1>MediumEdit About</h1>')

# def index(request):
#     return HttpResponse("Hello, world. You're at the MediumEdit index.")
# Create your views here.
