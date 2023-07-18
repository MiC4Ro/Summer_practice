from django.shortcuts import render, redirect
from users.models import Students
from creator.models import Quiz
from .forms import StudentForm

def index(request):
    student = Students.objects.all()
    return render(request, 'teacher/studentC.html', {'student': student})

def index_test(request):
    tests = Quiz.objects.all()
    return render(request, 'teacher/testC.html', {'tests': tests})

def index_stud(request):
    student = Students.objects.all()
    return render(request, 'teacher/studentC.html', {'student': student})

def create_student(request):
    error = ''
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-for-teacher')
        else:
            error = 'Форма неверно заполнена.'

    form = StudentForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'teacher/add-student.html', data)