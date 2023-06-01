from django.shortcuts import render

posts = [
    {
        'author': 'Ayush',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2023'
    },
    {
        'author': 'Jon',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogapp/home.html', context)


def about(request):
    return render(request, 'blogapp/about.html', {'title': 'About'})
