from django.shortcuts import render, redirect
from users.models import Students
from creator.models import Quiz
from .forms import createuserform

def index_test(request):
    tests = Quiz.objects.all()
    return render(request, 'teacher/testC.html', {'tests': tests})

def index_stud(request):
    student = Students.objects.all()
    return render(request, 'teacher/studentC.html', {'student': student})

def create_student(request):
    error = ''
    form=createuserform()
    if request.method=='POST':
        form = createuserform(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверно заполнена.'
    context={
        'form':form,
        'error':error
    }
    return render(request,'teacher/add-student.html',context)