import datetime
import random

from django.shortcuts import render

# Create your views here.

# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'pages/index.html')

def hello(request, name):
    context = {'name' : name}
    return render(request, 'pages/hello.html', context)

def lotto(request): # request는 임의로 지은 변수라 다른 이름으로 수정해도 됨
    print(request)
    print(type(request))
    print(request.META)
    # 로직
    numbers = sorted(random.sample(range(1, 46), 6))
    # 값을 딕셔너리에 담아서(보통 context라고 부름) 보낸다.
    context = {'numbers': numbers}
    # render 할때 3번째 인자로 넘겨준다.
    # render 함수의 필수 인자 : request, template 파일
    # 변수를 넘겨주고 싶으면 3번째 인자로 dictionary를 넘겨준다.
    # Django에서 활용하는 템플릿 언어는 Django Template Language(DTL)! Jinja와 비슷하지만 다른 언어
    return render(request, 'pages/lotto.html', context)

def dinner(request):
    menus = ['롯데리아', '편도', '맘스터치', '응급실떡볶이', '노은각', '피자', '치킨']
    pick = random.choice(menus)
    context = {
        'pick': pick, 
        'menus': menus,
        'users' : [],
        'sentence' : 'Life is short, You need Python + django!',
        'datetime_now' : datetime.datetime.now(),
        'google_link' : 'https://www.google.com'
        }
    return render(request, 'pages/dinner.html', context)


def cube(request, number):
    context = {
        'number': number,
        'number_cube': number ** 3,
        'numbers' : [1, 2, 3],
        'students' : {'지수': '지수!', '태수': '태수!'}
        }
    return render(request, 'pages/cube.html', context)


def about(request, name, age):
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'pages/about.html', context)

def isitgwangbok(request):
    now = datetime.datetime.now()
    if now.month == 8 and now.day == 15:
        result = True
    else:
        result = False
    context = {
        'result' : result
    }
    return render(request, 'pages/isitgwangbok.html', context)

def ping(request):
    return render(request, 'pages/ping.html')

def pong(request):
    # 사용자가 넘겨주는 값 받아오기
    print(request.GET) 
    # QueryDict 일종의 딕셔너리
    # {'data' : '안녕하세요'} 이런 형식으로 저장되어 있음
    data = request.GET.get('data')
    context = {
        'data': data
    }
    return render(request, 'pages/pong.html', context)

def signup(request):
    return render(request, 'pages/signup.html')

def signup_result(request):
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    pwcon = request.POST.get('pwcon')
    if pw == pwcon:
        is_signup = True
    else:
        is_signup = False
    context = {
        'is_signup' : is_signup,
        'id' : id
    }
    return render(request, 'pages/signup_result.html', context)