"""first_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 1. url 설정
# pages app의 views.py 파일 불러오기

urlpatterns = [
    path('admin/', admin.site.urls),
    # 각 앱 별로 따로 urls.py를 정의하여 관리함.
    path('pages/', include('pages.urls')), # django.urls에서 include를 가져옴
    path('services/', include('services.urls')),
]
