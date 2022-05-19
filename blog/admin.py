from django.contrib import admin
from blog.models import Tag, Post, Comment, AuthorProfile

#PostAdmin model
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# Registering models
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(AuthorProfile)