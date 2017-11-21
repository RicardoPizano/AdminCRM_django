# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from purchases.models import Purchases, Rate
from products.models import Product
from users.models import User

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
@csrf_exempt
def register_purchase(request):
    user_id = request.data['user_id']
    product_id = request.data['product_id']
    quantity = request.data['quantity']
    total = request.data['total']

    try:
        product = Product.objects.get(pk=product_id)
        user = User.objects.get(pk=user_id)
    except Product.DoesNotExist and User.DoesNotExist:
        return Response({'response': 0, 'errors': 'The product or user does not exist'})

    if product.stock > int(quantity):
        purchase = Purchases(user=user, product=product, quantity=quantity, total=total)
        purchase.save()
        product.stock = product.stock - int(quantity)
        product.save()
        return Response({'response': 1})
    else:
        return Response({'response': 0, 'errors': 'There are no products in stock'})


@api_view(['POST'])
@csrf_exempt
def register_rate(request):
    user_id = request.data['user_id']
    product_id = request.data['product_id']
    score = request.data['score']
    comment = request.data['comment']

    try:
        product = Product.objects.get(pk=product_id)
        user = User.objects.get(pk=user_id)
    except Product.DoesNotExist and User.DoesNotExist:
        return Response({'response': 0, 'errors': 'The product or user does not exist'})

    score = Rate(user=user, product=product, score=score, comment=comment)
    score.save()
    return Response({'response': 1})


@api_view(['GET'])
def get_product_rate(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'response': 0, 'errors': 'The product does not exist'})

    try:
        rates = Rate.objects.filter(product=product)
    except Rate.DoesNotExist:
        return Response({'response': 0, 'errors': 'This product does not have rate'})

    total = 0
    comments = []

    if rates > 0:
        for rate in rates:
            total += rate.score
            comments.append(
                {
                    'comment': rate.comment
                }
            )
        average = total / rates.count()

        response = {
            'product_id': product.pk,
            'product_name': product.name,
            'total_rate': total,
            'average': average,
            'comments': comments
        }
        return Response({'response': 1, 'product_rate': response})
    else:
        return Response({'response': 0, 'errors': 'This product does not have rate'})


@api_view(['GET'])
def view_my_purchases(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        purchases = Purchases.objects.filter(user=user)
        response = []
        for purchase in purchases:
            rate = get_rate(purchase.product, user)
            response.append({
                'name': purchase.product.name,
                'quantity': purchase.quantity,
                'unit_price': purchase.product.price,
                'total': purchase.total,
                'rate': rate
            })
        return Response({'response': 1, 'my_purchases': response})
    except User.DoesNotExist:
        return Response({'response': 0})


def get_rate(product, user):
    try:
        rate = Rate.objects.filter(user=user, product=product)
        return rate.score
    except Rate.DoesNotExist:
        return 0

