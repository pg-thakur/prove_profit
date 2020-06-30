from django.shortcuts import render ,redirect
from django import forms
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm

# Create your views here.
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    # fname= forms.CharField(max_length=254, required=True)
    class Meta:
        model = User
        fields = ('username', 'email' ,'password1', 'password2')

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('/')
    else:
        form= SignUpForm()
    

    return render(request,'accounts/signup.html',{'form':form})


def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request.POST)

        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            
            messages.error(request,'username or password not correct')
            return redirect('login')

    else:
        form = AuthenticationForm()

        return render(request,'accounts/login.html',{'form':form})

