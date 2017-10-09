# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from django.core.exceptions import ObjectDoesNotExist
from django.db import DataError, DatabaseError
from django.shortcuts import render

from purchases.models import Purchases, Rate

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
@csrf_exempt
def register_purchase(request):
    try:
        user_id = request.data['user_id']
        product_id = request.data['product_id']
        quantity = request.data['quantity']
        total = request.data['total']

        try:
            purchase = Purchases(user=user_id, porduct=product_id, quantity=quantity, total=total)
            purchase.save()
            return Response({'response': 1})
        finally:
            return Response({'response': 0, 'errors': 'Error in te data base'})

    finally:
        return Response({'response': 0, 'errors': 'Error in the data sending'})
