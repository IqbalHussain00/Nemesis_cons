from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages




def home(request):
    return render(request,'base.html')

def login(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email).username
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')


def signup(request):
    if request.method == 'POST':

        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save();
                messages.info(request,'user created')
                print('user created')
                return redirect('login') 
        
        else:
            messages.info(request,'password not matching..')
            return redirect('signup')

    else:
        return render(request,'signup.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def edit_un(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        username = request.POST['username1']
        new_username = request.POST['username2']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            user.username=new_username
            user.save()
            return redirect('/')
            
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')

    else:
        return render(request,'/')


def edit_e(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        email = request.POST['email']
        new_email = request.POST['new_email']
        password = request.POST['password']
        
        username = User.objects.get(email=email).username
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            user.email=new_email
            user.save()
            return redirect('/')
            
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')

    else:
        return render(request,'/')


def delete_e(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            user = User.objects.get(username=username)
            user.delete()
 
            user = User.objects.create_user(username=username,password=password)
            user.save();
            auth.login(request,user)
            return redirect('/')
            
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')

    else:
        return render(request,'/')
    


def delete_un(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            user = User.objects.get(username=username)
            email= User.objects.get(username=username).email
            user.delete()
 
            
            return redirect('/') 
            
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')

    else:
        return render(request,'/')
