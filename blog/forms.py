from .models import Comment
from django import forms
from .models import CoinType

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        


class CoinTypeForm(forms.ModelForm):



    coin_type = [
        ('BTC', 'Bitcoin'),
        ('LTC', 'Litecoin'),
        ('DOGE', 'Dogecoin'),
        ('XRP', 'Ripple'),
        ('ETH', 'Ethereum'),
        ('ADA', 'Cardano'),
        ('SHIB', 'Shiba Inu'),
        ('TRX', 'Tron'),
        ('NXT', 'Nxt'),
        ('DASH', 'Dash'),




    ]

    name = forms.ChoiceField(choices=coin_type, label='Cryptocurrency')




    class Meta:
        model = CoinType
        fields = ['name']
