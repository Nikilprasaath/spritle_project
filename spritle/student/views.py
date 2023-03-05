from django.shortcuts import render, redirect
from django.views import View
from django.template import loader      
from .forms import userform, calculationform
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from master.models import studenttasks



def is_student(request):
    if request.user.groups.filter(id =2):
        return True
    return False

class student_signup(View):
    def get(self,request):
        form = userform()
        context = {
            'form': form
        }
        return render(request,"student/templates/signup.html",context=context)

    def post(self,request):
    
        form = userform(request.POST)
        if form.is_valid():
            user=form.save()
            user.groups.add(2)
            user.save()
            form = userform()
        context  = {
            'form': form
        }
        return render(request,"student/templates/signup.html",context=context)
    

class loginview(View):
    def get(self, request):
        return render(request, 'student/templates/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            print(request.user)
            if user.groups.filter(id=2):
                login(request, user)
                print(request.user)
                return redirect('home')
            else:
                return render(request,'student/templates/login.html', {'error_message': "access denied"})
        else:
            return render(request, 'student/templates/login.html', {'error_message': 'Invalid login credentials'})
        

class logoutview(View):
    
    def get(self, request):
        logout(request)
        return redirect('login')
            
        
class calculator(View):

    def get(self, request):
        if request.user.is_authenticated:
            form = calculationform()
            context = {
                'form': form
            }
            return render(request,"student/templates/home.html",context)

        else:
            return redirect('login')
        
    def post(self, request):
        if request.user.is_authenticated:
            if is_student(request):
                form = calculationform(request.POST)
                if form.is_valid():
                    left_number = form.cleaned_data['left_number']
                    right_number = form.cleaned_data['right_number']
                    operand = form.cleaned_data['operand']

                    studenttasks.objects.create(student=request.user,left_number=left_number, right_number=right_number, operator=operand)

                    form = calculationform()

                context = {
                    'form':form
                }

                

                return render(request,"student/templates/home.html",context=context)
            
        return redirect('login')


class student_task_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            if is_student(request):
                activites = studenttasks.objects.filter(student=request.user)  
                context = {
                'activities': activites
                } 
                return render(request,"student/templates/activities.html",context=context)
            return HttpResponse("student access denied")
        return redirect('login') 
