from users.models import Students
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'last_name', 'email', 'password']