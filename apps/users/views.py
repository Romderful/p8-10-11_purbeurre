from django.shortcuts import redirect, render
from django.contrib.auth.models import User


# Create your views here.
def sign_up(request):
    """Sign up view."""
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password0 = request.POST["password0"]
        password1 = request.POST["password1"]
        if password0 == password1:
            if User.objects.filter(username=username).exists():
                print("Nom d'utilisateur déjà utilisé")
            elif User.objects.filter(email=email).exists():
                print("Email déjà utilisé")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password0
                )
                user.save()
                print("User created")
        else:
            print("Le mot de passe est différent")
        return redirect("/")
    else:
        return render(request, "signup.html")


def sign_in(request):
    """Sign in view."""
    return render(request, "signin.html")
