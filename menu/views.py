from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger
from .models import Menu, Category



def index(request):
    categories = Category.objects.order_by('position').filter(is_published=True)

    
    
    
    

    # menus = Menu.objects.order_by('category').filter(is_published=True)
    # categoryMenu = Category.objects.all()
    
    

    context = {
        # 'menus': menus,
        'categories': categories,
        
        
    }
    
    return render(request, 'pages/menu.html', context)


