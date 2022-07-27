from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import RegistrationForm, LoginForm


def create_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            user = User(**form.cleaned_data)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
        return redirect('books')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'user/registration.html', context=context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('books')
            else:
                return HttpResponseRedirect("/account/invalid/")
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'user/login.html', context=context)


def logout_user(request):
    auth.logout(request)
    return redirect('books')


# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'user/login.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context()
#         return dict(list(context.items()) + list(c_def.items()))
