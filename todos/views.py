from django.shortcuts import render, redirect
from django.contrib.auth.views import login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm
from todos.models import ToDo
from todos.serializers import ToDoSerializer


def index(request):
    if request.user.is_authenticated():
        return render(request,'todos/index.html')

    else:
        return login(request,template_name='todos/login.html')

def log_out(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('register')
    else:
        form = UserCreationForm()

        args = {'form':form}
        return render(request,'todos/reg_form.html',args)

class ToDoView(APIView):
    def get(self,request):
        todos = ToDo.objects.filter(user=request.user).order_by('deadline','priority')
        serializer = ToDoSerializer(todos,many=True)
        return Response(serializer.data)

    def post(self,request):
        _data = request.data.copy()
        _data['user'] = request.user.id
        print(_data)
        serializer = ToDoSerializer(data=_data)
        if serializer.is_valid():
            serializer.save()
            todos = ToDo.objects.filter(user=request.user).order_by('deadline','priority')
            serializer = ToDoSerializer(todos,many=True)
            return Response(serializer.data)
        
    def put(self,request):
        todo_id = request.data['id']
        todo = ToDo.objects.get(id=todo_id)
        if request.user == todo.user:
            print('JEE')
            print(request.data)
            serializer = ToDoSerializer(todo,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                todos = ToDo.objects.filter(user=request.user).order_by('deadline','priority')
                serializer = ToDoSerializer(todos,many=True)
                return Response(serializer.data)
            
