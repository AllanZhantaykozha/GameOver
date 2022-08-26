from django.contrib import admin
from .models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'steam')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'steam', 'release')
    fields = ('title', 'description', 'photo', 'release', 'create_by', 'category', 'cpu', 'gpu', 'ram', 'os', 'weight', 'steam', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    fields = ('title', 'description')


admin.site.register(Game, GameAdmin)
admin.site.register(Category, CategoryAdmin)

