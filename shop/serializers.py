from rest_framework import serializers
from .models import Category, Item

class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=20)
    code = serializers.CharField(max_length=8)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name = validated_data['category_name']
        instance.code = validated_data['code']
        instance.save()
        return instance



class ItemSerializer(serializers.Serializer):
    item_name = serializers.CharField(max_length=30)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.item_name = validated_data['item_name']
        instance.price = validated_data['price']
        instance.category_id = validated_data['category_id']
        instance.save()
        return instance

