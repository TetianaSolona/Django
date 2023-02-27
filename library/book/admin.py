from django.contrib import admin
from .models import Book
from author.models import Author



class BookAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'description', 'count', 'id', 'get_authors',)
    fields = ['name', 'description', 'count', 'id', ]
    list_filter = ('id', 'name', 'authors')
    search_fields = ('name', 'id')
    readonly_fields = ('id',)
    ordering = ('name',)


    Author.__str__ = lambda self:f'{self.name} {self.surname}'


    @admin.display(description='Authors')
    def get_authors(self, obj):
        return ', '.join([author.name + ' ' + author.surname for author in obj.authors.all()])
admin.site.register(Book, BookAdmin)
