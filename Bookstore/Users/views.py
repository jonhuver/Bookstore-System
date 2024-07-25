from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm,RegistrationForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
#import pydantic
from django.contrib.auth.views import LoginView

from .models import Users,UsersManager
from django.views.decorators.csrf import csrf_protect,csrf_exempt

from django.contrib.auth.models import User,BaseUserManager
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



def register_user(request):
    if request.method =='get' or "GET":
        print("got a get request for the create user  page")
        context = ''
        return render(request, 'signup.html')#, {'context': context}

    elif request.method == 'post' or "POST" :
        print("user request to create user")
        form = RegistrationForm(data = request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(form.password)

            user_details= Users(
                email=cd['email'],
                
                first_name=cd['first_name'],
                last_name=cd['last_name'],
               # user_contact=cd['user_contact'],
                username=cd['username']
                

                                        )
             
            
            

            user_details.save(False)
            password=request.POST.get('password')
            #print("username password",user_details.password)
#https://python.tutorialink.com/why-i-get-keyerror-exception-in-django-instead-of-this-field-is-required-exception-on-the-form-validation/
            user_details.set_password(password)
            print("username password",password)
            if " " in user_details.username:
             print("username has spce")

        
            if " " in user_details.password  :
               print("password has spce")
            user_details.save()
            
           # user = authenticate(username=user.username, password=request.POST['password1'])
           # login(request, user)

            success_url = reverse_lazy("login")


            return HttpResponseRedirect(success_url)


 # else:
           # context = {'error': 'Wrong credintials'}  # to display error?
            #print("context",context)
        else:
            
            print("invalid form")   # return render(request, 'registration/login.html')#, {'context': context}









def login_user(request,user=None):
   
    if request.method == 'get' or "GET":
        print("got a get request for the login page")
        context = ''
        return render(request, 'login.html')#, {'context': context}

    elif request.method == 'post' or "POST":
        print("got a POST request for the login page")
        username:str = request.POST.get('username')
        password:str = request.POST.get('password')

 
 
        print(f"entered username is: {username}\n and entred pass word is:{password}")

        user = authenticate(request, username=username, password=password)  #.strip
        if user is not None:
            login(request, user)
            

           
           
            #user=user.get_username()

            logged_in_user=Users.objects.get(username=username)

            #user_data=request.session

            #store the dtails of looged in user in session

            request.session['user'] =logged_in_user.username # request.POST

            print("successfully logged in as  " ,logged_in_user.username)

            success_url=reverse_lazy('dashboard')
            return HttpResponseRedirect(success_url)

            #return HttpResponse(f"successfulyy logged in as  {logged_in_user.email}")
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            print("context",context)
            return render(request, 'login.html')#, {'context': context}
        
def logout_user(request):
    # Logout user and redirect to home page
    logout(request)
    print("successfully logged out")
    return HttpResponse('successfully logged out')
   # return redirect("/")
   

 
    #return redirect("")





@login_required
def users_dashboard(request):
     
     

     if request.method == 'get' or "GET":
        print(f"accessing dashboard for logged in user {request.session['user']}")
     
        print("got a get request for the users dashboard page")
        context = ''
        return render(request, 'dashboard.html')#, {'context': co
     

     if request.method == 'post' or "POST":
        #print(f"accessing dashboard for logged in user {request.session['user']}")
     
       
        context = ''
        return render(request, 'dashboard.html')#, {'context': co
