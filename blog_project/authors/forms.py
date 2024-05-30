from django import forms
from authors.models import Author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Enter Your Name'})
        }