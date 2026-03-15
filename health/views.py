from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Disease, Remedy, HealthTip

def home(request):
    tips = HealthTip.objects.all()
    return render(request, 'home.html', {'tips': tips})

def diseases(request):
    data = Disease.objects.all()
    return render(request, 'diseases.html', {'diseases': data})

def remedies(request):
    data = Remedy.objects.all()
    return render(request, 'remedies.html', {'remedies': data})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
def diet(request):
    return render(request, 'diet.html')



def remedies_page(request):
    query = request.GET.get('q')  # Get search value

    if query:
        diseases = Disease.objects.filter(name__icontains=query)
    else:
        diseases = Disease.objects.all()

    context = {
        'diseases': diseases
    }

    return render(request, 'core/remedies.html', context)