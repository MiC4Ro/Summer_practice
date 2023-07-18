from django.urls import path
from . import views

urlpatterns = [
    path('tests/', views.quizzes, name="test-lib"),
    path('tests/add-test', views.create_quiz, name="add-test"),
    path('tests/<int:pk>', views.TestDetailView.as_view(), name='test-detail'),
    path('tests/add-test/add-question', views.create_question, name="add-question"),
    path('tests/add-test/add-question/add-answer', views.create_answer, name="add-answer"),
]