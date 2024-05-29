from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # exclude = ['roll']
        labels = {
            'roll': 'Student Roll',
            'name': 'Student Name',
            'father_name': "Father's Name"
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your Name'}),
            'roll': forms.NumberInput(attrs={'placeholder': 'Enter your roll number'})
        }

        help_texts = {
            'name': 'Write your full name'
        }

        error_messages = {
            'name' : {'required': 'your name is required'}
        }