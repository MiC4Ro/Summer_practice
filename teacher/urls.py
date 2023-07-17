from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('tests-for-teacher/', views.index_test),
    path('student-for-teacher/', views.index_student)
]


