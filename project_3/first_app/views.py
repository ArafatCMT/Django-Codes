from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'Author': 'rahim', 'Age' : 8 , 'bio':'Iam a Boy' , 'lst' : ['Python', 'is', 'Fun'], 'birthDay': datetime.datetime.now() ,'courses' : [
        {
            'id': 1,
            'course_name' : 'Python',
            'fee': 5000
        },
        {
            'id': 2,
            'course_name' : 'Django',
            'fee': 7000
        },
        {
            'id': 3,
            'course_name' : 'Data Structure',
            'fee': 12000
        },
        {
            'id': 4,
            'course_name' : 'Algorithm',
            'fee': 15000
        },
        {
            'id': 5,
            'course_name' : 'C',
            'fee': 5000
        }
    ]}
    # return render(request, 'first_app/home.html', context=d)
    # return render(request, 'first_app/home.html', {'Author': 'Rahim', 'Age' : 25})
    return render(request, 'first_app/home.html', d)
