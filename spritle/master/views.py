from django.shortcuts import render, redirect
from django.views import View
from .calculator import *
from django.template import loader      
from .forms import userform
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import studenttasks

def numbers(num):
    if num == 0 :
        return 'zero'
    elif num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    elif num == 9:
        return 'nine'

def operand_finder(op):
    if op == '+':
        return "plus"
    
    elif op == '-':
        return "minus"
    
    elif op == '*':
        return 'times'
    
    elif op == '/':
        return 'divided_by'


def is_master(request):
    if request.user.groups.filter(id=1):
        return True
    return False

        

class master_tasks(View):
    def get(self, request):
        if request.user.is_authenticated:
            if is_master(request):
                tasks = studenttasks.objects.filter(status="unsolved")
                context = {
                    'activities': tasks
                } 
                return render(request,"master/templates/tasks.html",context=context)
            return HttpResponse("master access denied")
        return redirect('master-login')
    
    def post(self, request):
        task_id = list(request.POST.keys())[1]
        obj = studenttasks.objects.get(id=task_id)
        left_number = numbers(obj.left_number)
        right_number = numbers(obj.right_number)
        operand = operand_finder(obj.operator)
        calculation = left_number + '(' + operand + '(' + right_number + '()))'
        result = eval(calculation)
        obj.calculation = calculation
        obj.result = result
        obj.status= "solved"
        obj.master = request.user
        obj.save()
        return redirect('master-tasks')


class master_solved(View):
    def get(self, request):
        if request.user.is_authenticated:
            if is_master(request):
                tasks = studenttasks.objects.filter(status="solved",master=request.user)
                context = {
                    'activities': tasks
                } 
                return render(request,"master/templates/solved_by_me.html",context=context)
            return HttpResponse("master access denied")
        return redirect('login')


class masterlogin(View):
    def get(self, request):
        return render(request, 'master/templates/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            if user.groups.filter(id=1):
                login(request, user)
                return redirect('master-tasks')
            else:
                return render(request,'master/templates/login.html', {'error_message': "Don't have master access"})
        else:
            return render(request, 'master/templates/login.html', {'error_message': 'Invalid login credentials'})
    
class logoutview(View):
    
    def get(self, request):
        logout(request)
        return redirect('master-login')
    

    
class master_signup(View):
    def get(self,request):
        form = userform()
        context = {
            'form': form
        }
        return render(request,"master/templates/signup.html",context=context)

    def post(self,request):
    
        form = userform(request.POST)
        if form.is_valid():
            user=form.save()
            user.groups.add(1)
            user.save()
            return redirect("master-login")

        context  = {
            'form': form
        }
        return render(request,"master/templates/signup.html",context=context)
