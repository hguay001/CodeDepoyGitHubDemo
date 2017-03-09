from django.shortcuts import render, get_object_or_404,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken import views as rest_framework_views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.

class ProfileStuff(APIView):
    def get(self,request):
        return Response(ProfileSerializer(request.user).data)

@permission_classes((AllowAny, ))      
class SignUp(APIView):
    def post(self,request):
        username = request.POST['username']
        if User.objects.filter(username=username):
            return Response({'error':'username already taken'})
        else:
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username,email,password)
            user.save()
            idx = User.objects.get(username=user.get_username()).pk
            token = Token.objects.raw('select * from authtoken_token where user_id={}'.format(idx))[0]
            return Response({'token':token.key})
        