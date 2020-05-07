from django.shortcuts import render


posts = [
    {
        'author': 'Demix',
        'title': 'Blog post 1',
        'content': 'Helllllllllllllllooooooooooo!!!!!!!!!!!!!!!!!',
        'date_posted': 'May 7, 2020'
    },
    {
        'author': 'Who',
        'title': 'Blog post 2',
        'content': 'HUHUHUAHDIuha!!',
        'date_posted': 'May 8, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
