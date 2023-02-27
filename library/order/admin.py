from django.contrib import admin
from .models import Order
from book.models import Book
from authentication.models import CustomUser




class OrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at', 'end_at', 'plated_end_at' )
    fields = ['book', 'user', 'created_at', 'end_at', 'plated_end_at' ]
    list_filter = ('user', 'book')
    search_fields = ('book', 'user')
    readonly_fields = ('created_at',)
    ordering = ('created_at',)

    Book.__str__ = lambda self:f'{self.name}'
    CustomUser.__str__ = lambda self:f'{self.email} FN:{self.first_name} LN:{self.last_name} Role:{self.role}'




admin.site.register(Order, OrderAdmin)