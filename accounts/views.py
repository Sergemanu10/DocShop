from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect


# Inscrire un User

User = get_user_model()

def signup(request):
    if request.method == "POST":

        # Traiter le formulaire

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/signup.html')


# Connecter un user

def login_user(request):
    if request.method == "POST":
        # Connecter un user
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Vérifier que les infos envoyées sont les bonnes
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'accounts/login.html')



# Déconnecter un User

def logout_user(request):
    logout(request)
    return redirect('index')