from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.quizzes),
    path('<int:pk>', views.TestDetailView.as_view(), name='test-detail'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('', views.home, name='home'),
]

