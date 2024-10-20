# api/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from django.shortcuts import render, redirect
from .forms import ItemForm
from django.http import JsonResponse


# API to get the list of items
class ItemListView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# API to get a single item by ID
class ItemDetailView(APIView):
    def get(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

# API to create a new item
class CreateItemView(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for creating a new item using a form
def create_item_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/api/items/')  # Redirect to the item list or any desired page
    else:
        form = ItemForm()

    return render(request, 'create_item.html', {'form': form})

def root_view(request):
    return JsonResponse({"message": "Welcome to the Django API root!", "admin": "/admin/", "itemList": "/api/items/", "itemDetails": "/api/items/1", "itemForm": "/api/items/form/", "createItem": "/api/items/create/"})