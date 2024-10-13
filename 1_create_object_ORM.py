import os
import django

# Укажите путь к settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'less_4.settings')
django.setup()

from myapp.models import Product

# Создаем три объекта Product
# Product.objects.create(name="Laptop", price=1000.00, quantity=10)
# Product.objects.create(name="Smartphone", price=500.00, quantity=25)
# Product.objects.create(name="Tablet", price=300.00, quantity=15)

# Запрашиваем все записи
products = Product.objects.all()
for product in products:
    print(product.name, product.price, product.quantity)