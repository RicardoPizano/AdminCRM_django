# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import ProductType, Product


@api_view(['GET'])
@csrf_exempt
def get_products_types(request):
    products_types = ProductType.objects.all()
    return Response({'response': 1, 'data': list(products_types.values())})


@api_view(['GET'])
@csrf_exempt
def get_products_types_by_id(request, product_type_id):
    try:
        product_type = ProductType.objects.get(pk=product_type_id)
        response = {
            'id': product_type.pk,
            'name': product_type.name,
            'description': product_type.description
        }
        return Response({'response': 1, 'product_type': response})
    except ProductType.DoesNotExist:
        return Response({'response': 0})


@api_view(['GET'])
@csrf_exempt
def get_products(request):
    products = Product.objects.all()
    return Response({'response': 1, 'data': list(products.values())})


@api_view(['GET'])
@csrf_exempt
def get_products_by_type(request, type_id):
    products = Product.objects.filter(product_type=type_id)
    return Response({'response': 1, 'data': list(products.values())})


@api_view(['GET'])
@csrf_exempt
def get_products_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        response = {
            'id': product.pk,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock,
            'product_type': product.product_type.name,
            'image': product.image
        }
        return Response({'response': 1, 'product': response})
    except Product.DoesNotExist:
        return Response({'response': 0})


@api_view(['POST'])
@csrf_exempt
def register_product_type(request):
    if request.method == 'POST':
        name = request.data['name']
        description = request.data['description']
        product_type = ProductType(name=name, description=description)
        product_type.save()
        return Response({'response': 1})


@api_view(['POST'])
@csrf_exempt
def register_product(request):
    if request.method == 'POST':
        try:
            name = request.data['name']
            description = request.data['description']
            price = request.data['price']
            stock = request.data['stock']
            product_type = ProductType.objects.get(pk=request.data['product_type'])
            image = request.data['image']
            product = Product(name=name, description=description, price=price, stock=stock, product_type=product_type,
                              image=image)
            product.save()
            return Response({'response': 1})
        except ProductType.DoesNotExist:
            return Response({'response': 0})


@api_view(['POST'])
@csrf_exempt
def update_product_type(request):
    if request.method == 'POST':
        product_type = ProductType.objects.get(pk=request.data['id'])
        if request.data['name'] != '':
            product_type.name = request.data['name']
        if request.data['description'] != '':
            product_type.description = request.data['description']
        product_type.save()
        return Response({'response': 1})


@api_view(['POST'])
@csrf_exempt
def update_product(request):
    if request.method == 'POST':
        product = Product.objects.get(pk=request.data['id'])
        if request.data['name'] != '':
            product.name = request.data['name']
        if request.data['description'] != '':
            product.description = request.data['description']
        if request.data['price'] != '':
            product.price = request.data['price']
        if request.data['stock'] != '':
            product.stock = request.data['stock']
        if request.data['product_type'] != '':
            product.product_type = request.data['product_type']
        if request.data['image'] != '':
            product.image = request.data['image']
        product.save()
        return Response({'response': 1})


@api_view(['POST'])
@csrf_exempt
def delete_product_type(request):
    if request.method == 'POST':
        product_type = ProductType.objects.get(request.data['id'])
        product_type.delete()
        return Response({'response': 1})


@api_view(['POST'])
@csrf_exempt
def delete_product(request):
    if request.method == 'POST':
        product = Product.objects.get(request.data['id'])
        product.delete()
        return Response({'response': 1})
