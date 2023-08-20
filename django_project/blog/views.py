from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html')

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html')

def contacts(request):
    return HttpResponse('<h3>Blog Contacts HAHA..</h3>')