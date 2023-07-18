from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tests-for-teacher/', views.index_test, name='tests-for-teacher'),
    path('student-for-teacher/', views.index_stud, name='student-for-teacher'),
    path('add-student/', views.create_student, name='add-student')
]


