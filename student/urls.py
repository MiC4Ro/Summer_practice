from django.urls import path
from . import views


urlpatterns = [
    path('', views.quizzes, name="test-lib-student"),
    path('<int:quiz_id>', views.display_quiz, name='display_quiz'),
    path('<int:quiz_id>/questions/<int:question_id>', 
    	views.display_question, name='display_question'),
    path('<int:quiz_id>/questions/<int:question_id>/grade/', 
    	views.grade_question, name='grade_question'),       
    path('results/<int:quiz_id>/', views.quiz_results, 
    	name='quiz_results'),
]

