from .models import Comment
from django import forms
from .models import CoinType

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        


class CoinTypeForm(forms.ModelForm):
    class Meta:
        model = CoinType
        fields = ['name']
