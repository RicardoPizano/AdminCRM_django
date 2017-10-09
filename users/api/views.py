# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from django.core.exceptions import ObjectDoesNotExist
from django.db import DataError, DatabaseError
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
        except:
            try:
                user = User.objects.get(mail=mail)
                return Response({'response': 0, 'errors': 'email already exists'})
            except:
                try:
                    user = User(name=name, last_name=last_name, nickname=nickname, mail=mail, password=password, user_type=0, is_active=True)
                    user.save()
                    return Response({'response': 1})
                except DataError as data_error:
                    return Response({'response': 0, 'errors': 'Error in the data sending'})
                except DatabaseError as database_error:
                    return Response({'response': 0, 'errors': 'Error in the data base'})

@api_view(['POST'])
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(nickname=username, password=password)
            if user.is_active == True:
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
                if user.is_active == True:
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
            except ObjectDoesNotExist as error:
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
