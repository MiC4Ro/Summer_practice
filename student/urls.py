from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizzes),
    path('<int:pk>', views.TestDetailView.as_view(), name='test-detail')
]