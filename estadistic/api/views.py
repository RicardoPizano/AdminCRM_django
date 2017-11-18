# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

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
        'five_stars': five_starts,
        'forth_stars': forth_starts,
        'tree_stars': tree_starts,
        'two_stars': two_starts,
        'one_stars': one_start
    }
    return Response({'response': 1, 'clients_feeling': response})


@api_view(['GET'])
def clients_quantity(request):
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
              'Octubre', 'Noviembre', 'Diciembre']
    clients = User.objects.all()
    today = datetime.today()
    first_total_add = 0
    second_total_add = 0
    third_total_add = 0
    fourth_total_add = 0
    fifth_total_add = 0
    first_total_delete = 0
    second_total_delete = 0
    third_total_delete = 0
    fourth_total_delete = 0
    fifth_total_delete = 0
    first_total = 0
    second_total = 0
    third_total = 0
    fourth_total = 0
    fifth_total = 0

    for client in clients:
        if not client.is_active:
            if client.delete_date.month == today.month:
                first_total_delete += 1
                first_total_add += 1
                first_total += 1
            if client.delete_date.month == today.month - 1:
                second_total_delete += 1
                second_total_add += 1
                second_total += 1
            if client.delete_date.month == today.month - 2:
                third_total_delete += 1
                third_total_add += 1
                third_total += 1
            if client.delete_date.month == today.month - 3:
                fourth_total_delete += 1
                fourth_total_add += 1
                fourth_total += 1
            if client.delete_date.month == today.month - 4:
                fifth_total_delete += 1
                fifth_total_add += 1
                fifth_total += 1
        else:
            if client.register_date.month == today.month:
                first_total_add += 1
                first_total += 1
            if client.register_date.month == today.month - 1:
                second_total_add += 1
                second_total += 1
            if client.register_date.month == today.month - 2:
                third_total_add += 1
                third_total += 1
            if client.register_date.month == today.month - 3:
                fourth_total_add += 1
                fourth_total += 1
            if client.register_date.month == today.month - 4:
                fifth_total_add += 1
                fifth_total += 1

    first_moth = {
        'month': months[today.month - 1],
        'total': first_total,
        'total_added': first_total_add,
        'total_deleted': first_total_delete

    }
    second_month = {
        'month': months[today.month - 2],
        'total': second_total,
        'total_added': second_total_add,
        'total_deleted': second_total_delete

    }
    third_month = {
        'month': months[today.month - 3],
        'total': third_total,
        'total_added': third_total_add,
        'total_deleted': third_total_delete

    }
    fourth_month = {
        'month': months[today.month - 4],
        'total': fourth_total,
        'total_added': fourth_total_add,
        'total_deleted': fourth_total_delete

    }
    fifth_month = {
        'month': months[today.month - 5],
        'total': fifth_total,
        'total_added': fifth_total_add,
        'total_deleted': fifth_total_delete

    }

    response = [first_moth, second_month, third_month, fourth_month, fifth_month]

    return Response({'response': 1, 'data': response})


@api_view(['GET'])
def products_quantity(request):
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
              'Octubre', 'Noviembre', 'Diciembre']
    products = Product.objects.all()
    today = datetime.today()
    first_total_add = 0
    second_total_add = 0
    third_total_add = 0
    fourth_total_add = 0
    fifth_total_add = 0
    first_total_delete = 0
    second_total_delete = 0
    third_total_delete = 0
    fourth_total_delete = 0
    fifth_total_delete = 0
    first_total = 0
    second_total = 0
    third_total = 0
    fourth_total = 0
    fifth_total = 0

    for product in products:
        if not product.is_active:
            if product.delete_date.month == today.month:
                first_total_delete += 1
                first_total_add += 1
                first_total += 1
            if product.delete_date.month == today.month - 1:
                second_total_delete += 1
                second_total_add += 1
                second_total += 1
            if product.delete_date.month == today.month - 2:
                third_total_delete += 1
                third_total_add += 1
                third_total += 1
            if product.delete_date.month == today.month - 3:
                fourth_total_delete += 1
                fourth_total_add += 1
                fourth_total += 1
            if product.delete_date.month == today.month - 4:
                fifth_total_delete += 1
                fifth_total_add += 1
                fifth_total += 1
        else:
            if product.register_date.month == today.month:
                first_total_add += 1
                first_total += 1
            if product.register_date.month == today.month - 1:
                second_total_add += 1
                second_total += 1
            if product.register_date.month == today.month - 2:
                third_total_add += 1
                third_total += 1
            if product.register_date.month == today.month - 3:
                fourth_total_add += 1
                fourth_total += 1
            if product.register_date.month == today.month - 4:
                fifth_total_add += 1
                fifth_total += 1

    first_moth = {
        'month': months[today.month - 1],
        'total': first_total,
        'total_added': first_total_add,
        'total_deleted': first_total_delete

    }
    second_month = {
        'month': months[today.month - 2],
        'total': second_total,
        'total_added': second_total_add,
        'total_deleted': second_total_delete

    }
    third_month = {
        'month': months[today.month - 3],
        'total': third_total,
        'total_added': third_total_add,
        'total_deleted': third_total_delete

    }
    fourth_month = {
        'month': months[today.month - 4],
        'total': fourth_total,
        'total_added': fourth_total_add,
        'total_deleted': fourth_total_delete

    }
    fifth_month = {
        'month': months[today.month - 5],
        'total': fifth_total,
        'total_added': fifth_total_add,
        'total_deleted': fifth_total_delete

    }

    response = [first_moth, second_month, third_month, fourth_month, fifth_month]

    return Response({'response': 1, 'data': response})
