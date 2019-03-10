from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from app01.models import *
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

        widgets = {
            "user": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "pwd": forms.widgets.PasswordInput(attrs={"class": "form-control"}),
            "age": forms.widgets.NumberInput(attrs={"class": "form-control"}),
            "hobby": forms.widgets.Textarea(attrs={"class": "form-control"}),
            "salary": forms.widgets.NumberInput(attrs={"class": "form-control"}),
        }
        error_messages = {
            "user": {
                "required": "用户名不能为空"
            },
            "pwd": {
                "required": "密码不能为空"
            },
            "age": {
                "required": "年龄不能为空"
            },
            "salary": {
                "required": "薪水不能为空"
            }
        }

        labels = {
            "user": "用户名",
            "pwd": "密码",
            "age": "年龄",
            "hobby": "爱好",
            "salary": "薪水",
        }

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method=="POST":
        name=request.POST.get("username")
        pwd=request.POST.get("password")
        print("=============>",name,pwd)

        user_obj = User.objects.filter(user=name,pwd=pwd).first()

        if user_obj:
            return redirect("/")

    return render(request,"login.html")

def users(request):
    users = User.objects.all()
    return render(request,"users.html",locals())

def user_add(request):
    userform = UserForm()
    if request.method=="POST":
        userform=UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('/users/')

    return render(request,"user_add.html",locals())

def user_edit(request,pk):
    userobj = User.objects.filter(pk=pk).first()
    userform = UserForm(instance=userobj)
    if request.method == "POST":
        userform = UserForm(request.POST,instance=userobj)
        if userform.is_valid():
            userform.save()
            return redirect('/users/')
    return render(request,"user_edit.html",locals())

def user_delete(request,pk):
    data = {"status":0,"msg":"删除失败,请再试一次"}
    obj=User.objects.filter(pk=pk).delete()
    if obj:
        data["status"] = 1
    return JsonResponse(data)

def testcss(request):

    return render(request,"testcss.html")
