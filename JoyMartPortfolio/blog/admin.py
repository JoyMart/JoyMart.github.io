from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    pass


class CategoyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoyAdmin)


