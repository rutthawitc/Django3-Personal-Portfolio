from django.contrib import admin
from .models import Blogs

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')

admin.site.register(Blogs, BlogsAdmin)
