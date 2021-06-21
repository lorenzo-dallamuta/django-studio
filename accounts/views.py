from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from .forms import LoginForm


class LoginUser(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username').strip()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})
