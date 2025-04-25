# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from .forms import CustomUserCreationForm
#
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('ads:list')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'users/register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # авторизация после регистрации
            return redirect('home')  # имя главной страницы
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Неверные данные'})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'users/home.html')