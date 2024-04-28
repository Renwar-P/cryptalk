from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        


""" the inspiration behind this codeblock came from [Freecode camp](https://www.youtube.com/watch?v=F5mRW0jo-U4) - Python Django Web Framework - Full Course for Beginners.
https://stackoverflow.com/questions/54415181/django-add-post-id-to-the-slug-only-if-it-already-exists
Python Django Web Framework - Full Course for Beginners.
[Codemy](https://codemy.com/) - Django Blog. 

"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'coin_type_name', 'coin_type_description', 'coin_type_max_cap', 'coin_creator']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['body'].required = True

   