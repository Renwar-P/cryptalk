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
        fields = ['title', 'body', 'coin_type_name', 'coin_type_description', 'coin_type_max_cap']



    def clean(self):
        cleaned_data = super().clean()
        coin_type_name = cleaned_data.get('coin_type_name')

        if coin_type_name == 'Other':
            raise forms.ValidationError("Please enter a valid coin type name.")

        return cleaned_data