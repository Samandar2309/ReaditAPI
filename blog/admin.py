from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    filter_horizontal = ('tags',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(About)
admin.site.register(Info)
admin.site.register(Clients)
admin.site.register(Comments)
