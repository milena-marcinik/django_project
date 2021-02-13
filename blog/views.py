from django.shortcuts import render


posts = [
    {
        'author': 'Milena',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 13, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 14, 2021'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request=request, template_name='blog/home.html', context=context)


def about(request):
    return render(request=request, template_name='blog/about.html', context={'title': 'About'})
