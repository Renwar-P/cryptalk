from .models import Comment
from django import forms
from .models import CoinType

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        


class CoinTypeForm(forms.ModelForm):

    COIN_CHOICES = [
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

    name = forms.ChoiceField(choices=COIN_CHOICES, label='Cryptocurrency')

    class Meta:
        model = CoinType
        fields = ['name']