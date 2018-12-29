from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from beauty.models import VIP


def go_reg(request):
    return render(request,'register.html')

def go_login(request):
    return render(request,'login.html')

def go_success(request):
    return render(request,'success.html')

def wrong_login(request):
    return render(request,'login.html',locals())

def register(request):
    regname = request.POST.get('regname')
    result = VIP.objects.filter(vipName=regname)
    if result:
        return HttpResponse('该用户名已被使用！！！')
    return HttpResponse('恭喜~~~可以注册')

def login(request):
    logname = request.POST.get('logname')
    logpwd = request.POST.get('logpwd')
    if logname == 'tom' and logpwd == '123456':
        request.session['logname'] = logname
        return redirect(reverse('beauty:success'))
    return redirect(reverse('beauty:wrong',args=('用户名或密码错误！',)))

