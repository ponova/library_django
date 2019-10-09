from django.contrib import admin
from .models import Author, Genre, Book

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'gender')
    list_filter = ('gender',)
    fields = [('first_name', 'last_name'), 'date_of_birth', 'gender']

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'title', 'dt_print', 'display_author', 'display_genre')
    fields = ['id', 'title', 'author', ('dt_print', 'genre', 'isbn')]
