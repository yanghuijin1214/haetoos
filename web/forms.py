from django import forms
from .models import Web
from login.models import User

class CommentForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    comment=forms.CharField(
        error_messages={
            'required':'내용을 입력해주세요.'
        },
        label='댓글 입력'
    )
    anony=forms.ChoiceField(widget=forms.Select(),
        choices=([('off','off'),('on','on'),]),label='익명',initial='off',required=True)
    content=forms.IntegerField(
        error_messages={
            'required':'강의를 입력해주세요'
        },
        label='강의',widget=forms.HiddenInput
    )
    def clean(self):
        cleaned_data=super().clean()

        comment=cleaned_data.get('comment')
        anony=cleaned_data.get('anony')
        content=cleaned_data.get('content')
        
        if not(comment and anony and content):
            self.add_error('comment','값이 없습니다.')
            self.add_error('anony','값이 없습니다.')