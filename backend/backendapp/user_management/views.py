from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
import random
from .models import User,Session
from .serializers import UserSerializer, SessionSerializer


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    body = json.loads(request.body)
    email = body.get('email', '')
    password = body.get('password', '')
    user = get_object_or_404(User, email=email, password=password)
    session_id = str(random.randint(1000000000, 9999999999))
    sessionData = {"session_id":session_id,"email":email}
    serializer = SessionSerializer(data=sessionData)
    if serializer.is_valid():
        serializer.save()
        data = {'detail':'success','message':None,'name': user.name,'email': user.email,'session_id': session_id,'id':user.id,'password':user.password}
        return JsonResponse(data)
    else:
        data = {'detail':'failed','message':'FAIL_ADD_SESSION','debug':'User Already logged in'}
        return JsonResponse(data)
    


@api_view(['POST'])
def check_session_view(request):
    body = json.loads(request.body)
    session_id = body.get('session_id', '')
    sessionData = get_object_or_404(Session, session_id=session_id)
    data = {'detail':'success','session_id': sessionData.session_id, 'email':sessionData.email}
    return JsonResponse(data)


@api_view(['POST'])
def logout_view(request, session_id):
    session = Session.objects.get(session_id=session_id)
    session.delete()
    data = {'detail':'success','message': 'USER_LOGGED_OUT'}
    return JsonResponse(data)



@api_view(['PUT'])
def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

