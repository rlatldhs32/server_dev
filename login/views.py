from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password #해시값으로암호화
from .serialize import LoginUserSerializer
# Create your views here.

class AppLogout(APIView):
    def post(self,request):

        return Response(status=200)

#실제로 로그인하는 것
class AppLogin(APIView):
    def post(self,request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        user = LoginUser.objects.filter(user_id=user_id).first()  # 있다면

        if user is None:
            return Response(dict(msg="해당 사용자가 없습니다."))

        if check_password(user_pw,user.user_pw): #클라이언트에서 온 패스워드 , db에서 올라온 패스워드 이게 같으면 트루
            return  Response(dict(msg="로그인 성공",user_id=user.user_id))
        #해당 유저의 값을 리턴해줌 디비에있는것과
        else:
            return  Response(dict(msg="로그인 실패, 비밀번호 틀림!"))

class RegistUser(APIView):
    def post(self,request):

        user_id = request.data["user_id"]
        user_pw = request.data["user_pw"]

        if user_id == '' or user_id == None or user_pw =='' or user_pw is None:
            return Response(data=dict(msg="아이디나 비밀번호는 공백이 될 수 없습니다."))

        user_pw=make_password(user_pw)

        if LoginUser.objects.filter(user_id=user_id).exists() :
            return Response(data=dict(msg="이미 존재하는 아이디입니다."))

        LoginUser.objects.create(user_id=user_id,user_pw=user_pw)

        return Response(data=dict(msg="회원가입에 성공했습니다.",user_id=user_id))


#
# class RegistUser(APIView):
#     def post(self,request):
#         #시리얼라이저있으면 필요없음!
#         serializer = LoginUserSerializer(request.data) #데이터가 바로 들어감
#
#         #클라에서 올리는것
#
#         user = LoginUser.objects.filter(user_id=serializer.data['user_id']).first() #있다면
#
#         if user is not None:
#             return Response(dict(msg="동일한 아이디가 있습니다."))
#
#         user = serializer.create(request.data)
#
#         return Response(data=LoginUserSerializer(user).data)
#     # 전송되니 views에서 db에 저장
