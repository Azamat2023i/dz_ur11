from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required


def index(request):
    advertisements = Advertisement.objects.all()
    cntext = {"advertisements": advertisements}
    return render(request, 'app_advertisments/index.html', cntext)

def top_sellers(request):
    return render(request, 'app_advertisments/top-sellers.html')

def advertisement(request):
    return render(request, 'app_advertisments/advertisement.html')

# ------

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request): 
    if request.method == "POST": 
        form = AdvertisementForm(request.POST, request.FILES) 
        if form.is_valid(): 
            advertisement = form.save(commit=False) 
            advertisement.user = request.user 
            advertisement.save() 
            url = reverse('advertisement_post') 
            return redirect(url) 
    else: 
        form = AdvertisementForm() 
    context = {'form': form} 
    return render(request, 'app_advertisments/advertisement-post.html', context)

# ------ 

def register(request):
    return render(request, 'app_ath/register.html')

# def login(request):
#     return render(request, 'app_ath/login.html')

# def profile(request):
#     return render(request, 'app_ath/profile.html')

