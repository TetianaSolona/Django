from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserForm
from .models import CustomUser

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are now Loged In"))
            return redirect('home')
            

        else:
            messages.success(request, ("There was an error logging in, Try again..."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logout!"))
    return redirect('home')

def register_user(request):

    if request.method == 'POST':
        userform = CustomUserForm(request.POST)
        if userform.is_valid():
            form = userform.save()
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                form.set_password(form.password)
                form.save()
                email = userform.cleaned_data['email']
                password = userform.cleaned_data['password']
                user = authenticate(email = email, password = password)
                login(request, user)
                messages.success(request, ("You Have Created a New Account!"))
                return redirect ('home')
            else:
                messages.success(request, ("Passwords do not Match, Please Try Again"))
                return redirect ('register_user')
        else:
            messages.success(request, ("This email is alredy taken, Please enter another..."))
            return redirect ('register_user')

    else:
        form = CustomUserForm
        return render(request, 'authenticate/register_user.html', {'form': form})


def all_users(request):
    users = CustomUser.get_all()
    context = {
        'users': users
        }
    return render (request, "authenticate/all_users.html", context=context)

def view_user (request, user_id):
    user = CustomUser.get_by_id(user_id)
    context = {
        'user': user
        }
    return render (request, 'authenticate/view_user.html',context=context)

