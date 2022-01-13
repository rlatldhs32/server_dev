"""server_dev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlp atterns:  path('blog/', include('blog.urls'))
"""#w장고는 실제로 여길 쳐다봄,
from django.contrib import admin
from django.urls import path,include


#머머머/login/머시기
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls'))  #메인폴더에서의 path가 연결해줌
]
