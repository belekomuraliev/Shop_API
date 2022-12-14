from django.shortcuts import render
from rest_framework import viewsets, request
from .models import Category, Item
from .serializers import CategorySerializer,ItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save(QR='3C350P42')