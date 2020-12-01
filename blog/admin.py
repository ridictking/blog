from django.contrib import admin

# Register your models here.
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    raw_id_fields = ('author',)
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    prepopulated_fields = {'slug': ('title',)}
