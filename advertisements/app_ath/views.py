from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_ath/profile.html')

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_ath/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_ath/login.html', {"error": "Пользователь не найден"})
        
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = UserCreationForm()
    return render(request, 'app_ath/register.html', {'form': form})
