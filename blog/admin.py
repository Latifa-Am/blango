from django.contrib import admin
from blog.models import Tag, Post

#PostAdmin class
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')

# Registering models
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
