from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField(label='Full Name :', required=False, help_text='Total length must be 70 character',
    widget=forms.Textarea(attrs = {'id': 'text_area', 'class': 'myClass', 'placeholder': 'Enter your full name'}))
    # file = forms.FileField()
    email = forms.EmailField(label='Email :', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    # age = forms.IntegerField(label='Age')
    # weight = forms.FloatField(label='Weight')
    # balance = forms.DecimalField(label='Balance')
    age = forms.CharField(label='Age', widget=forms.NumberInput)
    brithday = forms.CharField(label='Birth Date', widget=forms.DateInput(attrs={'type': 'date'}))
    check = forms.BooleanField(label='Check')
    appoinment = forms.DateTimeField(label='Appoinment', widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICE = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = forms.ChoiceField(choices=CHOICE, widget=forms.RadioSelect)
    MEAL = [('P','Pepperoni'), ('C', 'Chicken'), ('B', 'Beef'), ('M', 'Mashroom')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class studentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
        
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('your email must contain .com')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
        
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('your email must contain .com')

def if_Check(text):
    if len(text) < 10:
        raise forms.ValidationError("Enter a text with at least 10 characters")
class studentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator (message='your email must contain .com')])
    text = forms.CharField(validators=[if_Check])
    age = forms.IntegerField(validators=[validators.MinValueValidator(18, message='age must be at least 18'), validators.MaxValueValidator(35, message='age must be muximum 35')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['png'], message='file extension must be ended .png')])
        

class passwoedValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if val_password != confirm_password:
            raise forms.ValidationError("Password dosn't match")
        
        if len(val_name) < 10:
            raise forms.ValidationError("Enter a name with at least 10 characters")