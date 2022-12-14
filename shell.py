import json

from shop.models import Category, Item

with open('category.json', 'r') as file:
    category_data= json.load(file)

for category in category_data:
    Category.objects.create(**category)


with open('item.json', 'r') as file:
    item_data = json.load(file)


for item in item_data:
    Item.objects.create(**item)


