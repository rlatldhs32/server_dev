from django.shortcuts import render

# Create your views here.
# todo/views.py
from rest_framework.views import APIView
from .models import Task
from rest_framework.response import Response
from datetime import datetime
from django.shortcuts import render
#render : 화면에 뿌리는거
# ~/todo/views.py

class TaskSelect(APIView):
    def post(self,request):
        user_id = request.data.get('user_id',None)
        page_number=request.data.get('page_number',None)
        print("올라온 유저 아이디 :",user_id,page_number)

        if user_id and not "":
            #실습 3
            print("지금. 내 아이디 : ",user_id)
            tasks = Task.objects.filter(user_id=user_id)
        else:
            tasks = Task.objects.all()

        #페이지 처리
        is_last_page = True

        if page_number is not None and page_number >=0:
            if tasks.count()<=10:
                #첫페이지만 있을 때
                pass
            elif tasks.count() <=(1 + page_number) * 10 :#조회하고자 하는게  마지막페이지인가?
                tasks = tasks[page_number * 10:] #ㅔ이지가 0이면 : 0~9
                #어차피 이게 마지막페이지니까 뒤 인자가업음
            else:
                is_last_page=False
                tasks = tasks[page_number * 10:(1+page_number)*10]
                #tasks[0:10] ->0~9

        else:
            #실습 2
            pass

        task_list=[]

        for task in tasks:
            task_list.append(dict(id=task.id,
                                name=task.name,
                                userId=task.user_id,
                                done=task.done))


        return Response(status=200,data=dict(tasks=task_list,isLastPage=is_last_page))


##위에가 내가한거
class TaskCreate(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        todo_id = request.data.get('todo_id', "")
        name = request.data.get('name', "")

        if todo_id:
            task = Task.objects.create(id=todo_id, user_id=user_id, name=name)
        else:
            task =Task.objects.create(user_id=user_id, name=name)

        #보통 생성할때는, 응답값으로 만들어진 데이터를 줌
        return Response(data=dict(id=task.id)) #화면에 하나 쏘고, 서버에 하나 쏘고

class TaskToggle(APIView):
    def post(self,request):
        todo_id = request.data.get('todo_id',"")

        task = Task.objects.get(id=todo_id)

        if task:
            task.done = False if task.done is True else True
            task.save()

        return Response()





class Todo(APIView):
    def post(self, request): #post면, create하고 select 동시에함
        user_id = request.data.get('user_id', "")
        name = request.data.get('name', "")
        end_date = request.data.get('end_date', None)
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        Task.objects.create(user_id=user_id, name=name, end_date=end_date)

        tasks = Task.objects.all()
        task_list = []
        for task in tasks:
            task_list.append(dict(name=task.name, start_date=task.start_date, end_date=task.end_date, state=task.state))
        context = dict(task_list=task_list)

        return render(request, 'todo/todo.html', context=context)
    #response로 return 할 경우: json으로 줌 render : html로 주겠다. context는 dict(task_list) 이므로, 그걸 view에서 받아서
    #뿌림

    def get(self, request):
        tasks = Task.objects.all() #원래 필터걸었는데, 그냥 전체사용자 보여주게함
        task_list = []
        for task in tasks:
            task_list.append(dict(name=task.name, start_date=task.start_date, end_date=task.end_date, state=task.state))
        context=dict(task_list=task_list)
        return render(request, 'todo/todo.html', context=context)


class TaskDelete(APIView):
    def post(self,request):
        todo_id = request.data.get('todo_id', "")

        task= Task.objects.get(id=todo_id)

        if task:
            task.delete()

        return Response()


# # Create your views here.
# class TaskCreate(APIView):
#     def post(self, request):
#         user_id = request.data.get('user_id', "")
#         name = request.data.get('name', "")
#         end_date = request.data.get('end_date', None)
#         if end_date:
#             end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
#         task = Task.objects.create(user_id=user_id, name=name, end_date=end_date)
#
#         return Response(dict(msg="To-Do 생성 완료", name=task.name, start_date=task.start_date.strftime('%Y-%m-%d'), end_date=task.end_date))
#
# #
# class TaskSelect(APIView):
#     def post(self, request):
#         user_id = request.data.get('user_id', "")
#
#         tasks = Task.objects.filter(user_id=user_id)
#
#         task_list=[]
#
#         for task in tasks:
#
#             task_list.append(dict(name=task.name,start_date=task.start_date,end_date=task.end_date,state=task.state))
#
#         return Response(dict(tasks=task_list))