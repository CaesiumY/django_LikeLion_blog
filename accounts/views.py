from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # 생략 가능
from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

# Create your views here.

# 기본 로그인, 로그아웃, 회원가입 클래스

# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.get(username=request.POST['username'])
#                 return render(request, 'signup.html', {'error': 'Username has already been taken'})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(
#                     username=request.POST['username'], password=request.POST['password1'])
#                 auth.login(request, user)
#                 return redirect('home')
#         else:
#             return render(request, 'signup.html', {'error': 'Passwords must match'})
#     else:
#         return render(request, 'signup.html')


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'username or password is incorrect.'})
#     else:
#         return render(request, 'login.html')


# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('home')
#     return render(request, 'login.html')
#     # auth.logout(request)
#     return redirect('home')


# django에서 지원해주는 로그인, 로그아웃, 회원가입 클래스

class LoginViews(LoginView):
    template_name = 'login.html'


login = LoginViews.as_view()


class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL


logout = LogoutViews.as_view()


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, })
