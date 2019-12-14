from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Corey',
        'title': 'The little big man',
        'content': 'This is the beginning of a great story',
        'date_posted': 'October 11, 1193'
    },
    {
        'author': 'Dodley',
        'title': 'The Big little man',
        'content': 'This is the end of a great story',
        'date_posted': 'October 11, 2193'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})