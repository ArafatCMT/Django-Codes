from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name','Rahim')
    # response.set_cookie('name', 'Karim', max_age=60*3)
    response.set_cookie('name', 'Karim', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name': name})

def delete_cookie(request):
    respone = render(request, 'del.html')
    respone.delete_cookie('name')
    return respone

def set_session(request):
    # data = {
    #     'name': 'Rahim',
    #     'age': '25',
    #     'language': 'Bangla'
    # }
    # print(request.session.get_session_cookie_age()) #session koto time thikbe seta daker jonno
    # print(request.session.get_expiry_date()) # session koto din thikbe seta daker jonno
    # request.session.update(data)
    request.session['name'] = 'rahim'
    return render(request, 'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Guest')
        # age = request.session.get('age')
        return render(request, 'get_session.html', {'name': name})
    else:
        return HttpResponse('Your session has been expired.Login again')

def delete_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'del.html')