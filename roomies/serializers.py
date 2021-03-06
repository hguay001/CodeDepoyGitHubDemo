from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')