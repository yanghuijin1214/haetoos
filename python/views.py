from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView,FormView
from django.utils.decorators import method_decorator #데코레이터
from login.decorators import login_check
from .models import Python,Python_comment
from login.models import User
from .forms import CommentForm
from django.db import transaction
# Create your views here.

@method_decorator(login_check,name='dispatch')
class PythonList(ListView):
    model=Python
    template_name="python_list.html"
    context_object_name='python_list' #html로 넘겨줄 model 객체 이름 정하기

@method_decorator(login_check,name='dispatch')
class PythonDetail(DetailView):
    template_name='python_detail.html'
    queryset=Python.objects.all()
    context_object_name='python'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['comment']=Python_comment.objects.filter(content=self.kwargs.get('pk')) #url의 pk 값 읽어오기
        context['form']=CommentForm(self.request)
        return context

    
@method_decorator(login_check,name='dispatch')
class CommentWrite(FormView):
    form_class = CommentForm
    template_name='python_detail.html'

    def form_valid(self,form):
        with transaction.atomic():
            python_comment=Python_comment(
                content=Python.objects.get(pk=form.data.get('content')),
                comment=form.data.get('comment'),
                user=User.objects.get(haetoos_id=self.request.session.get('user')),
                anony=form.data.get('anony'),
            )
            python_comment.save()
        self.success_url='/lecture/python/'+str(form.data.get('content'))
        return super().form_valid(form)

    def form_invalid(self, form):  # form 이 invalid한 경우. error 가 있을 경우
        # form.product 값은 id임
        return redirect('/lecture/python/'+str(form.data.get('content')))


    def get_form_kwargs(self, **kwargs):
        # 기존에 formview에 있는 함수를 호출해서 먼저 만들어줌.
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        # kw에 request를 추가해서 반환
        return kw