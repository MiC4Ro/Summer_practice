from django.shortcuts import render

def base(request):
    students_programms = {
        'a': ['Алгоритмы и структуры данных', '2']
    }
    return render(request, 'student/base.html', students_programms)