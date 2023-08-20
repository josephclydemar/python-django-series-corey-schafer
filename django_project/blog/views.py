from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'This is first blog post',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 1',
        'content': 'This is second post content',
        'date_posted': 'December 18, 2020'
    },
    {
        'author': 'Joseph Clyde Mar',
        'title': 'Blog Post 3',
        'content': 'This is third blog content',
        'date_posted': 'July 11, 2023'
    }
]

# Create your views here.
def home(request):
    context = {
                'title': 'HomePage',
                'posts': posts }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', { 'title': 'About Hehe' })

def contacts(request):
    return HttpResponse('<h3>Blog Contacts HAHA..</h3>')