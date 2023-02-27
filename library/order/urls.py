from django.urls import path
from . import views

urlpatterns = [

    path('all_orders/', views.all_orders, name="all_orders"),
    path('create_order/<int:book_id>', views.create_order, name="create_order"),
    path('end_order/<int:order_id>', views.end_order, name="end_order"),
    path('delete_order/<int:order_id>', views.delete_order, name="delete_order"),

    ]