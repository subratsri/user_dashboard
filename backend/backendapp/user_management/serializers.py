from rest_framework import serializers
from .models import User, Session


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')  

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('session_id','email')  
