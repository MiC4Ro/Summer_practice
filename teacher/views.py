from django.shortcuts import render


def index(request):
    data = {
        'title': 'преподователи',
    }
    return render(request, 'teacher/base.html', data)

def index_test(request):
    data = {

    }
    return render(request, 'teacher/testC.html', data)

def index_student(request):
    return render(request, 'teacher/studentC.html', {'user': user})