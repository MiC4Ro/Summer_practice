from django.urls import path
from . import views

urlpatterns = [
    path('tests/', views.quizzes, name="test-lib"),
    path('tests/add-test', views.create_quiz, name="add-test"),
    path('tests/<int:pk>', views.TestDetailView.as_view(), name='test-detail'),
    path('tests/<int:pk>/update', views.TestUpdateView.as_view(), name='test-update'),
    path('tests/<int:pk>/delete', views.TestDeleteView.as_view(), name='test-delete'),
    path('tests/answers/<int:pk>', views.QustionDetailView.as_view(), name='question-detail'),
    path('tests/answers/<int:pk>/update', views.QuestionUpdateView.as_view(), name='question-update'),
    path('tests/answers/<int:pk>/delete', views.QuestionDeleteView.as_view(), name='question-delete'),
    path('tests/answer/<int:pk>/update', views.AnswerUpdateView.as_view(), name='answer-update'),
    path('tests/answer/<int:pk>/delete', views.AnswerDeleteView.as_view(), name='answer-delete'),
    path('tests/add-test/add-question', views.create_question, name="add-question"),
    path('tests/add-test/add-question/add-answer', views.create_answer, name="add-answer"),
]