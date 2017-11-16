from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(Language)
#admin.site.register(BookInstance)



# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    search_fields = ['first_name']

# Register the admin class with the associated model

# Register the Admin classes for Book using the decorator

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'due_back')
    search_fields = ['title']
    list_filter = ('due_back', 'genre')
    inlines = [BooksInstanceInline]
    
    
    fieldsets = (
        (None, {
            'fields': ('title', 'isbn','summary','genre', 'pub_date')
        }),
        ('Availability', {
            'fields': ('due_back','author')
        }),
    )



@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book','status' , 'borrower')
    search_fields = ['book']
    list_filter = ('status', 'borrower')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'borrower')
        }),
    )








    
    
 