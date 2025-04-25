from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    AdListView, 
    AdDetailView, 
    ad_create, 
    my_ads, 
    ad_delete,
    home
)

app_name = 'ads'

urlpatterns = [
    path('', AdListView.as_view(), name='ad_list'),
    path('home/', home, name='home'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('create/', ad_create, name='ad_create'),
    path('my/', my_ads, name='my_ads'),
    path('delete/<int:pk>/', ad_delete, name='ad_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)