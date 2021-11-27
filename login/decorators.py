from django.shortcuts import redirect
from .models import User

def login_check(function):
    def wrap(request,*args,**kwargs):
        user=request.session.get('user')
        if user is None or not user:
            return redirect('/') #로그인페이지로 redirect
        return function(request,*args,**kwargs)
    return wrap

'''
def admin_check(function):
    def wrap(request,*args,**kwargs):
        user=request.session.get('user')
        if user is None or not user:
            return redirect('/') #로그인페이지로 redirect
        else:
            #print(user)
            a=User.objects.get(haetoos_id=user)
            if a.level=='user':
                return redirect('/')
        return function(request,*args,**kwargs)
    return wrap
'''
