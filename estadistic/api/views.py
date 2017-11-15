# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count

from purchases.models import Purchases, Rate
from products.models import Product
from users.models import User

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def clients_feeling(request):
    rates = Rate.objects.all()
    five_starts = 0
    forth_starts = 0
    tree_starts = 0
    two_starts = 0
    one_start = 0

    for rate in rates:
        if rate.score == 5:
            five_starts += 1
        if rate.score == 4:
            forth_starts += 1
        if rate.score == 3:
            tree_starts += 1
        if rate.score == 2:
            two_starts += 1
        if rate.score == 1:
            one_start += 1

    response = {
        '5_stars': five_starts,
        '4_stars': forth_starts,
        '3_stars': tree_starts,
        '2_stars': two_starts,
        '1_stars': one_start
    }
    return Response({'response': 1, 'clients_feeling': response})