from .models import Quiz, Question, Answer
from django.forms import ModelForm

class QuizForm(ModelForm):
    class Meta:
        model= Quiz
        fields = ['name']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'qtype', 'explanation', 'quiz']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['name', 'is_correct', 'question']