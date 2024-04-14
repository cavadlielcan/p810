from django.contrib import admin

from .models import Blog,Author

# admin.site.register(Blog)
admin.site.register(Author)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'view_count')