from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=20, verbose_name='Название категории')
    code = models.CharField(max_length=8, verbose_name='Код категории')

    def __str__(self):
        return self.category_name

class Item(models.Model):
    item_name = models.CharField(max_length=30, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Стоимость товара')
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
