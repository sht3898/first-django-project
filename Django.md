# Django 수업 정리

##  isitgwangbok

오늘이 광복절인지 여부를 나타내는 웹 페이지

### 1) url 정의

```python
path('isitgwangbok/', views.isitgwangbok),
```



### 2) View 정의

```python
def isitgwangbok(request):
    now = datetime.datetime.now() # now에 현재 시간 저장
    if now.month == 8 and now.day == 15: # 월이 8, 일이 15인지 확인하여 결과 저장
        result = True
    else:
        result = False
    context = {	# context에 result 저장
        'result' : result
    }
    return render(request, 'isitgwangbok.html', context)
```



### 3) 템플릿 정의 (REAME.md의 dinner 참조)

```html
<body>
  <h1>{{ result }}</h1>
  <h2>{% now 'm/d' %}</h2>
      <!-- now 현재 시간
    `m/d`을 통해 월/일 출력
    =>django 문법(Built-in tags)
    'Y/m/d'로 하면 연/월/일 출력
 -->
</body>
```



### 4) 서버 실행 및 확인

```bash
$ python manage.py runserver
```

![1565670127532](./images/gwangbok.png)





## ping / pong으로 신호 주고 받기

### 1) url 정의

```python
path('ping/', views.ping)
path('pong/', views.pong)
```

