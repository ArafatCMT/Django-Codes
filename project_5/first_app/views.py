from django.shortcuts import render
from . forms import ContactForm, studentForm, passwoedValidationProject

# Create your views here.
def home(request):
    return render(request,'./first_app/home.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request,'./first_app/about.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request,'./first_app/about.html')

def submit_form(request):
    # print(request.POST)
    # if request.method == 'POST':
    #     name = request.POST.get('username')
    #     email = request.POST.get('email')
    #     return render(request,'first_app/form.html', {'name': name, 'email': email})
    # else:
    return render(request,'./first_app/form.html')

def Django_forms(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name , 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)

            print(form.cleaned_data)
            # return render(request, './first_app/django_form.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, './first_app/django_form.html', {'form': form})


def student_data(request):
    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = studentForm()
    return render(request, './first_app/django_form.html' ,{'form': form})


def passwordValidation(request):
    if request.method == 'POST':

        form = passwoedValidationProject(request.POST)
        if form.is_valid():
            print(form.changed_data)
    else:
        form = passwoedValidationProject()
    return render(request, './first_app/django_form.html' , {'form': form})