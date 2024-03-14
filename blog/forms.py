from .models import Comment, Post
from django import forms
from .models import CoinType
from .models import AuthorImage

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

class AuthorImageForm(forms.ModelForm):
    
    image = forms.ImageField()
    class Meta:
        model = AuthorImage
        fields = ['image']


""" the inspiration behind this codeblock came from [Freecode camp](https://www.youtube.com/watch?v=F5mRW0jo-U4) - Python Django Web Framework - Full Course for Beginners.
https://stackoverflow.com/questions/54415181/django-add-post-id-to-the-slug-only-if-it-already-exists
Python Django Web Framework - Full Course for Beginners.
[Codemy](https://codemy.com/) - Django Blog. 

"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'coin_type', 'featured_image', 'author_image']

