# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from purchases.models import Rate
from users.models import User


@api_view(['POST'])
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        name = request.data['name']
        last_name = request.data['last_name']
        nickname = request.data['nickname']
        mail = request.data['mail']
        password = request.data['password']

        try:
            user = User.objects.get(nickname=nickname)
            return Response({'response': 0, 'error': 'nickname already exists'})
        except User.DoesNotExist:
            try:
                user = User.objects.get(mail=mail)
                return Response({'response': 0, 'errors': 'email already exists'})
            except User.DoesNotExist:
                user = User(name=name, last_name=last_name, nickname=nickname, mail=mail, password=password,
                            user_type=0, is_active=True)
                user.save()
                return Response({'response': 1})


@api_view(['POST'])
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(nickname=username, password=password)
            if user.is_active:
                return Response({
                    'response': 1,
                    'data': {
                        'id': user.pk,
                        'name': user.name,
                        'last_name': user.last_name,
                        'nickname': user.nickname,
                        'mail': user.mail,
                        'user_type': user.user_type
                    }
                })
            else:
                return Response({'response': 0, 'errors': 'the user has been deleted'})
        except ObjectDoesNotExist:
            try:
                user = User.objects.get(mail=username, password=password)
                if user.is_active:
                    return Response({
                        'response': 1,
                        'data': {
                            'id': user.pk,
                            'name': user.name,
                            'last_name': user.last_name,
                            'nickname': user.nickname,
                            'mail': user.mail,
                            'user_type': user.user_type
                        }
                    })
                else:
                    return Response({'response': 0, 'errors': 'the user has been deleted'})
            except ObjectDoesNotExist:
                return Response({'response': 0, 'errors': 'Username or password incorrect'})


@api_view(['POST'])
@csrf_exempt
def update_user(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.data['id'])
        if request.data['name'] != '':
            user.name = request.data['name']
        if request.data['last_name'] != '':
            user.last_name = request.data['last_name']
        if request.data['password'] != '':
            user.name = request.data['password']
        user.save()
        return Response({'response': 1})


@api_view(['POST'])
@csrf_exempt
def delete_user(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.data['id'])
        user.is_active = False
        user.save()
        return Response({'response': 1})


@api_view(['POST'])
@csrf_exempt
def view_profile(request):
    try:
        user = User.objects.get(pk=request.data['user_id'])
        response = {
            'name': user.name,
            'last_name': user.last_name,
            'nickname': user.nickname,
            'email': user.mail,
            'user_type': user.user_type
        }
        return Response({'response': 1, 'user': response})
    except User.DoesNotExist:
        return Response({'response': 0, 'error': 'The user does not exist'})


@api_view(['POST'])
@csrf_exempt
def get_users_by_type(request):
    user_type = request.data['user_type']
    users = User.objects.filter(user_type=user_type)
    if users.count() > 0:
        response = []
        for user in users:
            if user.is_active:
                response.append(
                    {
                        'id': user.pk,
                        'name': user.name,
                        'last_name': user.last_name,
                        'nickname': user.nickname,
                        'email': user.mail,
                        'register_date': user.register_date,
                        'user_type': user.user_type,
                        'is_active': user.is_active
                    }
                )
        return Response({'response': 1, 'users': response})
    else:
        return Response({'response': 0})


@api_view(['GET'])
@csrf_exempt
def get_products_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        user_purchases = user.purchases_set.all()
        response = []
        for purchase in user_purchases:
            rate = Rate.objects.get(user=user, product=purchase.product)
            response.append({
                'name': purchase.product.name,
                'quantity': purchase.quantity,
                'price': purchase.product.price,
                'total': purchase.total,
                'rate': rate.score,
                'comment': rate.comment
            })
        return Response({'response': 1, 'user_purchases': response})
    except User.DoesNotExist:
        return Response({'response': 0})
