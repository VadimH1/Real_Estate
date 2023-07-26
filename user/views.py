from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ProfileSerializer
from .models import User, Profile
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.exceptions import ValidationError
from django.core.mail import send_mail
from Real_Estate.settings import EMAIL_HOST_USER
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from uuid import uuid4
import uuid

from user import serializers


def index(request):
    return render(request, 'index1.html')


class UserRegistration(APIView):
    def get(self, request):
        return render(request, 'register.html')
    

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = serializer.validated_data

        user = User.objects.filter( email = user_data['email']).first()

        if user:
            return Response({"message": "User with this email already exist"}, 400)

        new_user = User.objects.create(
            email = user_data['email'],
            first_name = user_data['first_name'],
            last_name = user_data['last_name'],
            password = make_password(user_data['password']),
            uuid_number = uuid.uuid4()
        )
        
        new_user.save()

        new_profile = Profile.objects.create(
            user_profile=new_user
        )
        new_profile.save()

        send_mail(
            subject="Your registration to the Real_Estate",
            message=f"We inform you that you have successfully registered on our Real Estate website. You have verified your email address. To activate follow this link http://127.0.0.1:8000/activate/{new_user.uuid_number}",
            from_email=EMAIL_HOST_USER,
            fail_silently=False,
            recipient_list=['vadim17gal@gmail.com'],
        )

        return Response({"Status": f"SignUp has been successfully {new_user}, {new_profile}"}, 200)    
    

class UserLogin(APIView):
    def get(self, request):
        return render(request, 'login.html')  
   

class ProfileApiView(APIView): #???????
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        user = User.objects.filter(id=user_id).first()
        serializer = UserSerializer(user)
        profile_serializer = ProfileSerializer(user.profile)
        return Response({"Profile":profile_serializer.data, "User":serializer.data}, 200) 
         

class ActivateApiView(APIView):

    def get(self, request, user_uuid_number):
        return render(request, 'user_activate.html')
    

    def put(self, request, user_uuid_number):

        user = User.objects.filter(uuid_number = user_uuid_number).first()
        if not user:
            return ({"Error": "Account is active"}, 200)
        user.is_active = True
        user.save()

        return Response({"Status": "Activated user "f"{user}"}, 200)
    

class ChangeEmailApiView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass

    def put(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = serializer.validated_data
        old_user_email = User.objects.filter(email=user_data['email']).first()
        if old_user_email:
            return Response({"error": "User with this email already exist"})

        user = User.objects.filter(pk=request.user.id).first()
        
        user.email = user_data['email']
        # if check_password(password_user_entered, request.user.password):
        # You can authenticate
        if not check_password(user_data['password'], user.password):
            return Response({"error": "You entered the wrong password"}, 400)
        
        user.save()

        return Response({"status": "Successful change of email address"}, 200)
    
class ChangePasswordApiView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        pass


    def put(self, request, data):

        user_id = request.user.id
        serializer = UserSerializer(data=request.data)
        old_password = data['old_password']
        user = User.objects.filter(id=user_id).first()
        if not check_password(old_password, user.password):
                return Response({"old_password": "[ Wrong password ]"}, 400)
        serializer.is_valid()
        data = serializer._validated_data
        user.set_password(data['password'])
        user.save()
        return Response({"status": "Successful change password"}, 200)


        # user_id = request.user.id
        # serializer = UserSerializer(data=request.data)

        # user = User.objects.filter(id=user_id).first()

        # # data = serializer.validated_data
        # if serializer.is_valid():
        #     if not user.check_password(serializer.data.get('old_password')):
        #         return Response({"old_password": "[ Wrong password ]"}, 400)
        #     user.set_password(serializer.data.get("new_password"))
        #     user.save()
        #     response = {
        #         'status': 'success',
        #         'code': 200,
        #         'message': 'Password updated successfully',
        #         'data': []
        #     }

        #     return Response(response)
        # return Response(serializer.errors, 400)
    
        