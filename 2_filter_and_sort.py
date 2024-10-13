import os
import django

# Указываем путь к settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'less_4.settings')
django.setup()

from myapp.models import Product

# Пример использования filter(), exclude() и order_by()
# Продукты с ценой больше 500
products = Product.objects.filter(price__gt=500)
print("Продукты с ценой больше 500:")
for product in products:
    print(product.name, product.price)

# Исключаем продукты с ценой меньше 500
products = Product.objects.exclude(price__lt=500)
print("\nПродукты с ценой не меньше 500:")
for product in products:
    print(product.name, product.price)

# Сортируем продукты по цене по возрастанию
products = Product.objects.order_by('price')
print("\nПродукты, отсортированные по цене (по возрастанию):")
for product in products:
    print(product.name, product.price)