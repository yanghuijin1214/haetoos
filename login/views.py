from django.shortcuts import render,redirect

# from django.contrib.auth import authenticate
from .models import User
from django.contrib.auth.hashers import make_password, check_password

#User import? https://wayhome25.github.io/django/2017/05/18/django-auth/

# Create your views here.
def index(request):
    return render(request,'login/index.html')

def sign_in(request):
    if request.method == 'GET':
        return render(request,'login/sign_in.html')

    elif request.method == 'POST':
        haetoos_id = request.POST['haetoos_id']
        haetoos_ps = request.POST['haetoos_ps']

        if not haetoos_id or not haetoos_ps:
            message = 'type id and password'
            return render(request,'login/sign_in.html', {'message':message})

        try:
            person = User.objects.get(haetoos_id=haetoos_id)
        except User.DoesNotExist:
            message = 'account doesn\'t exist'
            return render(request,'login/sign_in.html', {'message':message})

        if check_password(haetoos_ps,person.haetoos_ps):
            message = 'logined Succesfully!'
            request.session['user']=person.haetoos_id
        else:
            message = 'wrong id or password'
            return render(request,'login/sign_in.html',{'message': message})

        return redirect('/lecture/python/')


def sign_up(request) :
    if request.method == 'GET':
        return render(request,'login/sign_up.html')

    elif request.method =='POST':
        res = {}
        #id ps 입력 안한 경우, 비밀번호가 불일치
        haetoos_id =request.POST['haetoos_id'] ; haetoos_ps = request.POST['haetoos_ps']
        if not haetoos_id or not haetoos_ps:
            res['message'] = 'please type id and password'
            return render(request,'login/sign_up.html',res)
        elif haetoos_ps != request.POST['haetoos_ps2']:
            res['message'] = 'passwords don\'t match'
            return render(request,'login/sign_up.html',res)
        else:
            name = request.POST['name']
            student_id = request.POST['student_id']
            try: 
                person = User.objects.get(student_id = student_id)
            except: #학번이 등록되어 있지 않은 경우
                res['message'] = 'Failed to Create. Ask manager to join the club'
                return render(request,'login/sign_up.html',res)

        #가입 가능 및 저장
        if name != person.name:
            res['message'] = 'wrong name'
            return render(request,'login/sign_up.html',res)

        person.haetoos_id = haetoos_id
        person.haetoos_ps = make_password(haetoos_ps)
        person.phone_number=request.POST['phone_number']

        person.save()
        res['message'] = 'Create Succesfully!'
        return render(request,'login/sign_in.html',res)        

def result(request) :
    return render(request,'login/result.html')
