from django.urls import re_path
from .views import RegistUser, AppLogin

# ~/login/regist_user 하면 수행됨
urlpatterns = [
    re_path('regist_user', RegistUser.as_view(), name='regist_user'),
    re_path('app_login', AppLogin.as_view(), name='app_login')
    # 사용자가 regist_user로 호출할 경우에,  view에서 만든 RegistUser이 수행됨. View로써.
]
