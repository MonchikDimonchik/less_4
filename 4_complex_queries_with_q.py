import os
import django
from django.db.models import Q

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'less_4.settings')
django.setup()

from myapp.models import Product

# Пример с использованием AND
products_and = Product.objects.filter(Q(price__gt=500) & Q(quantity__lt=20))
print("Продукты с ценой > 500 и количеством < 20:", products_and)

# Пример с использованием OR
products_or = Product.objects.filter(Q(price__gt=1000) | Q(quantity__gt=30))
print("Продукты с ценой > 1000 или количеством > 30:", products_or)

# Сложный запрос с использованием AND и OR
products_complex = Product.objects.filter(Q(price__lt=500) | (Q(quantity__gt=10) & Q(price__gte=300)))
print("Сложный запрос:", products_complex)