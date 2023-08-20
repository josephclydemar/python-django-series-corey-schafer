from django.shortcuts import render
# from django.http import HttpResponse

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
                'posts': posts
              }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
                'title': 'About Hehe',
                'about_me': '''
                            DHKDS Hello there! I'm John Doe, a curious soul and a dedicated writer on a journey to share my thoughts, experiences, and insights through this blog.
                            From a young age, I've been captivated by the power of words and their ability to shape ideas, connect people, and inspire change. My passion for storytelling and exploration has led me on an exciting path of discovery.
                            My blog is a reflection of my diverse interests, ranging from technology and science to art and philosophy. Join me as I dive into the intricacies of the digital world, ponder the mysteries of the universe, and contemplate the beauty that surrounds us.
                            When I'm not immersed in writing, you can find me sipping on a cup of freshly brewed coffee, lost in a good book, or wandering through nature's wonders.
                            '''
              }
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', context)

def contacts(request):
    # return HttpResponse('<h3>Blog Contacts HAHA..</h3>')
    return render(request, 'blog/contacts.html', { 'title': 'Contacts' })