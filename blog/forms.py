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
  
    custom_coin_type = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Post
        fields = ['title', 'body', 'coin_type_name', 'coin_type_description', 'coin_type_max_cap', 'featured_image', 'author_image', 'custom_coin_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        coin_choices = CoinType.objects.values_list('name', 'name')
        
        coin_choices = list(coin_choices)
        coin_choices.append(('Other', 'Other'))

       
        self.fields['coin_type_name'].choices = coin_choices

    def clean(self):
        cleaned_data = super().clean()
        coin_type_name = cleaned_data.get('coin_type_name')
        custom_coin_type = cleaned_data.get('custom_coin_type')

        
        if coin_type_name == 'Other' and not custom_coin_type:
            raise forms.ValidationError("Please enter a custom coin type.")
        
        return cleaned_data

