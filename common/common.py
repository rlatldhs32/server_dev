from rest_framework.response import Response
from rest_framework.views import APIView


# 사용할 user_id기능
# 싱크가 안맞을때있기때문에 API 버전을 알려주는것도 필요
class TodoView(APIView):
    user_id = ''
    version = ''

    def dispatch(self, request, *args, **kwargs):
        # 헤더에 값을 넣어놨으니, 그
        # 헤더에 버전이랑 값을 넣어주면, 그 디스패치 함수가 실행될때
        # dispatch가 실행될때 버전이랑 아이디를 넣어둠
        self.user_id = request.headers.get('id', False)
        self.version = request.headers.get('version', False)

        return super(TodoView, self).dispatch(request, *args, **kwargs)

    # todoView를 상속한 클래스가 실행이 되면, dispatch 작동할때 저게 작동되고,
    # dispatch가 끝나면
    # 그상위에있는, APIView에 있는 원래 디스패치를 동작시키라는 말임super << 부모객체


def CommonResponse(result_code, result_msg, data):
    return Response(status=200,
                    data=dict(
                        result_code=result_code,
                        result_msg=result_msg,
                        data=data
                        )
                    )

def SuccessResponse():
    return Response(status=200,
                    data=dict(
                        result_code=0,
                        result_msg="success"
                    ))


def SuccessResponseWithData(data):
    return Response(status=200,
                    data=dict(
                        result_code=0,
                        result_msg="success",
                        data=data
                    ))


def ErrorResponse():
    return Response(status=200,
                    data=dict(
                        result_code=999,
                        result_msg="error!!!"
                    ))
