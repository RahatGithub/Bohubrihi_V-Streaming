from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from App_Accounts.forms import CreateNewUser
from App_Accounts.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm  # to authenticate the user's credential 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required

def sign_up(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile(user=user)
            user_profile.save() 
            return HttpResponseRedirect(reverse('App_Accounts:log_in'))  # change it to 'App_Post:home', also pass user info when logged in 
    
    context={ 'title':'Sign up . V-Stream', 'form' : form }

    return render(request, 'App_Accounts/signup.html', context)


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
                return HttpResponseRedirect(reverse('App_Posts:home')) 
    
    context={'title':'Login . V-Stream', 'form':form}

    return render(request, 'App_Accounts/login.html', context)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Accounts:log_in'))