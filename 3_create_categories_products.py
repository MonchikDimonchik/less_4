import os
import django

# Указываем путь к settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'less_4.settings')
django.setup()

from myapp.models import Category, Product

# Создаем несколько категорий
# category1 = Category.objects.create(name="Electronics")
# category2 = Category.objects.create(name="Furniture")

# Создаем несколько продуктов
# Product.objects.create(name="Laptop", price=1000.00, quantity=10, category=category1)
# Product.objects.create(name="Smartphone", price=500.00, quantity=25, category=category1)
# Product.objects.create(name="Tablet", price=300.00, quantity=15, category=category1)
# Product.objects.create(name="Chair", price=100.00, quantity=50, category=category2)
# Product.objects.create(name="Table", price=200.00, quantity=30, category=category2)


category = Category.objects.get(name="Electronics")
products = category.product_set.all()

for product in products:
    print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")


categories = Category.objects.all()

for category in categories:
    print(f"Category: {category.name}")
    for product in category.product_set.all():
        print(f"  Product: {product.name}, Price: {product.price}")


# Используем values() для получения только нужных полей
products = Product.objects.values('name', 'price')
for product in products:
    print(f"Name: {product['name']}, Price: {product['price']}")

# Используем values_list() для получения списка значений
product_names = Product.objects.values_list('name', flat=True)
print("Product names:", list(product_names))