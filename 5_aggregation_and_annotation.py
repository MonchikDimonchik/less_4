import os
import django
from django.db.models import Count, Sum, Min, Max

# Укажите путь к settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'less_4.settings')
django.setup()

from myapp.models import Category, Product

# Аннотация: количество продуктов в каждой категории через связь product
categories = Category.objects.annotate(num_products=Count('product'))
print("\nКоличество продуктов в каждой категории:")
for category in categories:
    print(f"Категория: {category.name}, Количество продуктов: {category.num_products}")

# Агрегация: общая сумма цен всех продуктов
total_price = Product.objects.aggregate(Sum('price'))
print(f"\nОбщая сумма цен всех продуктов: {total_price['price__sum']}")

# Агрегация: минимальная и максимальная цена продуктов
min_max_price = Product.objects.aggregate(Min('price'), Max('price'))
print(f"\nМинимальная цена продукта: {min_max_price['price__min']}")
print(f"Максимальная цена продукта: {min_max_price['price__max']}")