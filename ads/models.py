from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

User = get_user_model()

class Ad(models.Model):
    CATEGORY_CHOICES = [
        ('Транспорт', 'Транспорт'),
        ('Недвижимость', 'Недвижимость'),
        ('Работа', 'Работа'),
        ('Услуги', 'Услуги'),
        ('Личные вещи', 'Личные вещи'),
        ('Для дома и дачи', 'Для дома и дачи'),
        ('Электроника', 'Электроника'),
        ('Хобби и отдых', 'Хобби и отдых'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='ads/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('ads:ad_detail', kwargs={'pk': self.pk})