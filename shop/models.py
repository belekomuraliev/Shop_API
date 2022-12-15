from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название категории')
    description = models.CharField(max_length=50, verbose_name='Код категории')

    def __str__(self):
        return self.name

class Item(models.Model):
    item_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30, verbose_name='Название товара')
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Стоимость товара')
    QR = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.name} - {self.price} - {self.item_id}'
