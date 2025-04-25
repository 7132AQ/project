from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import profile, user_logout

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
