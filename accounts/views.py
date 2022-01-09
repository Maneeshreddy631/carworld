from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request) :
    if request.method == 'POST' :
        username = request.POST['username']  #we take username andpassword from user
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password) #it takes and authenticate with database
        if user is not None :
            auth.login(request,user)
            messages.success(request,'You are now Logged in!')
            return redirect('dashboard')
        else :
            messages.error(request,'Invalid Login credentials')
            return redirect('login')
    return render(request , 'accounts/login.html')


def register(request) :
    if request.method == 'POST' :
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password :
            if User.objects.filter(username=username).exists() :
                messages.error(request,'Username already exists!')
                return redirect('register')
            else :
                if User.objects.filter(email=email).exists() :
                    messages.error(request,'Email already exists!')
                    return redirect('register')
                else :
                    user =User.objects.create_user(first_name = firstname,last_name=lastname,username = username ,email=email,password = password)
                    auth.login(request,user)
                    messages.success(request,'You are now logged in')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request,'You are registered succesfully')
                    return redirect('login')
#by defULT DJANGO USES SH8 HASHING TECHNIQUE SO PASS PASSWORD ASIT IS IT WILL BE HASHED
        else :
            messages.error(request ,'password doesnot match')
            return redirect('register')

    else :
        return render(request,'accounts/register.html')
    return render(request , 'accounts/register.html')

@login_required(login_url = 'login')
def dashboard(request) :
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)  # this is where e will be getting logged in user id and we will ferch the contacts corresponding to thet user id
    data =  {
        'inquiries' :  user_inquiry,
    }
    return render(request , 'accounts/dashboard.html',data)


def logout(request) :
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are successfully logged out.')
        return redirect('home')

    return redirect('home')