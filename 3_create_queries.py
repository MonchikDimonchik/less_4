import os
import django

# Указываем путь к settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'less_4.settings')
django.setup()

from myapp.models import Category, Product

# Пример 1: Получить все продукты из категории Electronics
category = Category.objects.get(name="Electronics")
products = category.product_set.all()

print("Продукты из категории Electronics:")
for product in products:
    print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

# Пример 2: Получить категории с их продуктами
categories = Category.objects.all()

print("\nКатегории и их продукты:")
for category in categories:
    print(f"Category: {category.name}")
    for product in category.product_set.all():
        print(f"  Product: {product.name}, Price: {product.price}")

# Пример 3: Используем values() для получения только имен и цен продуктов
products = Product.objects.values('name', 'price')
print("\nИмена и цены продуктов:")
for product in products:
    print(f"Name: {product['name']}, Price: {product['price']}")

# Пример 4: Используем values_list() для получения списка имен продуктов
product_names = Product.objects.values_list('name', flat=True)
print("\nСписок имен продуктов:", list(product_names))