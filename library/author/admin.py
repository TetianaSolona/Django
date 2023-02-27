from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic')
    fields = ['name', 'surname', 'patronymic']
    list_filter = ('id', 'name')
    search_fields = ('name', 'id', 'surname')



admin.site.register(Author, AuthorAdmin)