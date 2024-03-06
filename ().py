# coding: utf-8
from blog.models import CoinType
CoinType.objects.filter(name='BTC').update(max_cap='Max Supply: 21M')
