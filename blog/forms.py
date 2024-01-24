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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        coin_choices = CoinType.objects.values_list('name', 'name')
        self.fields['name'].choices = coin_choices






