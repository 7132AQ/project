from django.db import models
from django.conf import settings  # Вот здесь магия

class Advertisement(models.Model):
    CATEGORIES = [
        ('goods', 'Товары'),
        ('services', 'Услуги'),
        ('property', 'Недвижимость'),
        ('transport', 'Транспорт'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads')
    image = models.ImageField(upload_to='ads/', null=True, blank=True)

    def __str__(self):
        return self.title
