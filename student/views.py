from django.shortcuts import render
from creator.models import Quiz, Question
from django.views.generic import DetailView


def quizzes(request):
    quizzes = Quiz.objects.all()
    questions = Question.object.all()
    context = {'quizzes': quizzes,
               'questions': questions}
    return render(request, 'student/base.html', context)

class TestDetailView(DetailView):
    model = Quiz
    template_name = 'student/test.html'
    context_object_name = 'quizzes'