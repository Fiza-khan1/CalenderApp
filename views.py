from django.shortcuts import render,redirect
from .forms import EventForm,sign_up,LoginForm
from django.contrib import messages,redirects
from django.contrib.auth import authenticate,login,logout
from .models import Events
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def sign_in(request):
    if request.method=='POST':
        form=sign_up(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Sign Up created successfully')
        else:
            messages.error(request,'Some errors occur ')
    form=sign_up()
    return render(request,'sign_in.html',{'form':form})

def FormCalender(request):
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            form.save()
            event = form.save(commit=False)  
            print("REQUET",request.user) 
            event.person=request.user
            print(event)
            print("event.perosn",event.person)
            event.save()      
            messages.success(request,'Event added Successfully')
        else:
            messages.error(request,"Correct the errors below")
    form=EventForm()
    return render(request,'base.html',{'form':form})

def userlogin(request):
    if request.method=='POST':
                        form=LoginForm(request,request.POST)
                        if form.is_valid():
                            print('form',form)
                            username = form.cleaned_data['username']
                            print('username',username)
                            password = form.cleaned_data['password']
                            print('passeorf',password)
                            user=authenticate(request,username=username,password=password)
                            print('user',user)
                            if user is not None:
                                print(user)
                                login(request,user)
                                messages.success(request,'Login Created Successfully')   
                                return redirect('home')           
                            else:
                                messages.error(request,'Correct Some errors below')

        
      
    form=LoginForm()
    return render(request,'login.html',{'form':form})


def userlogut(request):
    logout(request)
    messages.success(request,'You are logged Out')
    return redirect('login')

def dashboard(request):
     event=Events.objects.all()
     print(event)
     return render(request,'displayEvent.html',{'Event':event})


def EditEvent(request,id):
     person1=Events.objects.filter(id=id)
     if request.method=='POST':
          form=EventForm(request.POST)
          if form.is_valid():
               person=form.cleaned_data['person']
               day=form.cleaned_data['day']
               start_date=form.cleaned_data['start_date']
               end_date=form.cleaned_data['end_date']
               notes=form.cleaned_data['notes']
               print('person',person)
               print('day',person)
               print('start_date',start_date)
               print('end_date',end_date)
               print('notes',notes)
               student=person1.update(person=person,day=day,start_date=start_date,end_date=end_date,notes=notes)
               messages.success(request,'Form updated SUccessfully')
               return redirect('dashboard')     
     form=EventForm()
     return render(request,'edit.html',{'form':form})

def deleteEvent(request,id): 
        person=Events.objects.filter(id=id)
        person.delete()
        return redirect('dashboard')
def deleting(request):
       if request.method=='POST':
         if 'yes' in request.POST:
          check=request.POST['name']
          print("Check value",check)
          if check=='yes':         
                person=Events.objects.filter(id=id)
                person.delete()
          return redirect('dashboard')
         
def Profile(request,id):
     user=User.objects.get(id=id) 
     return render(request,'profile.html',{'User':user})





