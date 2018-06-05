from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http.response import JsonResponse
from .models import User
from hashlib import md5
from django.core.exceptions import ObjectDoesNotExist
import json


# Create your views here.

@require_POST
def login(requset):
    username = requset.POST.get('username')
    password = requset.POST.get('password')

    if username is None:
        return JsonResponse({'code': 0, 'message': '请输入账号！'})

    if password is None:
        return JsonResponse({'code': 0, 'message': '请输入密码！'})

    md = md5(password.encode(encoding='utf-8'))
    password_md5 = md.hexdigest()



    try:
        user = User.objects.values('id', 'userName', 'trueName', 'phone', 'email').get(userName=username, password=password_md5)
        user_str = requset.session.get('login_user')
        if user_str:
            return JsonResponse({'code': 2, 'message': '用户已登录！'})
        requset.session['login_user'] = json.dumps(user)
        return JsonResponse({'code': 1, 'message': '登录成功!'})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code': 0, 'message':'账号/密码错误'})

