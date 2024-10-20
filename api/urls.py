# api/urls.py
from django.urls import path
from .views import ItemListView, ItemDetailView, CreateItemView, create_item_view

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/create/', CreateItemView.as_view(), name='item-create'),
    path('items/form/', create_item_view, name='item-form'),  # New URL for form
]
