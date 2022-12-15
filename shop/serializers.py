from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data['id']
        instance.name = validated_data['category']
        instance.description = validated_data['description']
        instance.save()
        return instance



    def validate_name(self, value):
        for i in value:
            if i in '!@#$%^&*':
                raise serializers.ValidationError('В name не должно содержать  такие символы как !@#$%^&*')
        return value



class ItemSerializer(serializers.ModelSerializer):
    # item_id = serializers.CharField(max_length=10)
    # name = serializers.CharField(max_length=30)
    # category_id = serializers.IntegerField()
    # price = serializers.IntegerField()
    #QR = serializers.CharField(max_length=10, validators='get_qr',)


    class Meta:
        model = Item
        fields = '__all__'
        read_only_fields = ['QR',]


    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.item_id = validated_data['item_id']
        instance.name = validated_data['name']
        instance.category = validated_data['category']
        instance.price = validated_data['price']
        #instance.QR = validated_data['item_id'], validated_data['price'], validated_data['item_id']
        instance.save()
        return instance

    def validate_name(self, value):
        for i in value:
            if i in '!@#$%^&*':
                raise serializers.ValidationError('В name не должно содержать  такие символы как !@#$%^&*')
        return value
