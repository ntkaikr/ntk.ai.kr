# accounts/views.py
from django.shortcuts import render, redirect
from .forms import BootstrapUserCreationForm

def signup(request):
    if request.method == "POST":
        form = BootstrapUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = BootstrapUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
