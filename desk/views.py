from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import DeskOfFile
# Create your views here.

def login(request):

    return render(request, "registration/login.html")

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("fileDesk")
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {"form": form})
@login_required(login_url='/desk/login/')
def fileDesk(request):
    fileToShow = DeskOfFile.objects.all()


    context = {
        "fileToShow": fileToShow,

    }
    return render(request, 'filedesk.html', context)
