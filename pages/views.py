from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Menu

def index(request):
    featured_menu = Menu.objects.all().filter(featured_listing=True)

    context = {
        'featured_menu' : featured_menu
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
