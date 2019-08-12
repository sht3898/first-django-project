# Django

장고라 발음한다, 디장고 아님



## 성격

Opinionated(다소 독선적)

자유분방하게 할 수 있는 것이 적다



## 프레임워크

* framework => 어떤 서비스를 만들때 사용되는 소스 코드의 집합

  ex) django

* library => framework등에서 특정 기능만을 수행하기 위한 소스 코드들

   framework와 비슷한 듯하면서도 다름

  ex) bootstrap



## Dynamic Web





## MTV

Model : 데이터를 관리

Template : 사용자가 보는 화면

View : 중간 관리자



## 가상환경 생성

git bash에서

```bash
python -m venv 가상환경이름
```

venv  폴더 ignore 처리

```bash
vi .gitignore

venv/
```

활성화

```bash
source venv/Scripts/activate
```

잔고 설치

```bash
pip install django
```

설치여부 확인

```bash
pip list
```

pip 업그레이드

```bash
python -m pip install --upgrade pip
```



여기까지 했었는데 다시 deactive 하고 설치

```bash
deactivate
venv
pip install django
python -m pip install -upgrade pip
```

django 프로젝트 시작

```bash
django-admin startproject first_django .

python manage.py runserver
```

localhost:8000 을 입력하여 실행



## 한국어/ 한국 시간 설정

`settings.py`에서 맨 밑에 있는 LAGUAGE_CODE = 'ko-kr'로 설정하고, TIME_ZONE='Asia/Seoul' 로 수정



## 기타

urls.py : url 정의

views.py : 함수 정의

templates/__.html : 템플릿 정의





## 1. 시작하기

```bash
$ pip install django
```

* 현재 활용하고 있는 버전은 다음과 같다.
  * python 3.7.4
  * django 2.2.4

### 1. Django 프로젝트 시작

```bash
$ mkdir __프로젝트 이름 or 폴더 이름 __
$ cd __프로젝트 이름 or 폴더 이름__
```

```bash
$ django-admin startproject __프로젝트이름__ .
```
프로젝트 이름 뒤에 뛰어 쓰기를 하고 점(.)을 써야함.

* 프로젝트 이름으로 구성된 폴더와, manage.py가 생성된다.
  * `__init__.py` : 해당 폴더가 패키지로 인식될 수 있게끔 작성되는 파일
  * `settings.py` : **django 설정과 관련된 파일**
  * `urls.py` : **url 관리**
  * `wsgi.py` : 배포시 사용(web server gateway interface : 파이썬에서 사용되는 웹 서버)
  * `manage.py` : django 프로젝트와 관련된 커맨드라인(명령어) 유틸리티

### 2. 서버 실행

```bash
$ python manage.py runserver
```

* `localhost:8000` 으로 들어가서 로켓 확인!







### 3.  App 생성

```bash
$ python manage.py startapp __app이름__
```

* `app이름`인 폴더가 생성되며, 구성하고 있는 파일은 다음과 같다.

  * `admin.py` : 관리자 페이지 설정

  * `apps.py` : app의 정보 설정. 직접 수정하는 경우 별로 없음.

  * `models.py` : **MTV-Model을 정의하는 곳**

  * `tests.py` : 테스트 코드를 작성하는 곳.

  * `views.py` : **MTV-View를 정의하는 곳.**

    * 사용자에게 요청이 왔을 때, 처리되는 함수

      ```python
      def index(request):
          return render(request, index.html)
      ```

**app을 만들고 나서 반드시 `settings.py`에서 `INSTALLED_APPS`에 app을 등록한다.**

```python
# first_django/settings.py
# ..
INSTALLED_APPS = [
    'pages',
    'django.contrib.admin',
    # ...
]
#..
```

## 2. 작성 흐름

### 1. URL 정의

```python
# first_django/urls.py
from pages import views

urlpatterns = [
    path('', views.index), # django에서는 끝에 계속 콤마 쓰는 연습
]
```

* `urls.py`는 우리의 웹 어플리케이션 경로들을 모두 관리한다.
* 요청이 들어오면 `urls.py`의 `urlpatterns`에 정의된 경로에 매핑한다.
* path(`경로`, `views에 정의된 함수`)

### 2. View 정의

```python
# pages/views.py

def index(request):
    return render(request, 'index.html')
```

* `views.py`는 MTV에서 View에 해당한다.
* 일종의 중간관리자로 Model, Template 등의 처리를 담당한다.



### 3. Template 정의

* 기본적으로 app을 생성하면, `templates` 폴더가 없으므로 직접 생성해야 한다.

```html
<!-- pages/templates/index.html -->
<h1>
    장고 안녕!
</h1>
```



### 4. 서버 실행 및 확인

```bash
$ python manage.py runserver
```

`localhost:8000` 에서 확인해보자!

