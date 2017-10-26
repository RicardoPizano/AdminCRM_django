# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from purchases.models import Purchases, Rate
from products.models import Product

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
        except Product.DoesNotExist:
            return Response({'response': 0, 'errors': 'The product does not exist'})

        if product.stock > quantity:
            purchase = Purchases(user=user_id, porduct=product_id, quantity=quantity, total=total)
            purchase.save()
            product.stock = product.stock - quantity
            product.save()
            return Response({'response': 1})
        else:
            return Response({'response': 0, 'errors': 'There are no products in stock'})
