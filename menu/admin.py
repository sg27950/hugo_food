from django.contrib import admin
from .models import Menu, Category


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'featured_listing', 'is_published',
                    'price', 'list_date')
    list_display_links = ('id', 'title')
    # list_filter = ('category', )
    list_editable = ('is_published', 'featured_listing')
    search_fields = ('id', 'title', 'featured_listing', 'is_published'
                     'price', 'list_date', 'description')
    list_per_page = 25


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25


    


admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
