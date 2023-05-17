from rest_framework.views import APIView
from .models import Announcement, User
from rest_framework.response import Response
from django.forms import model_to_dict
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view



def index(request):
    return render(request, "estate/index.html")


@api_view(["GET", "POST"])
def register(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user_email = User.objects.filter(email=email)

        if user_email:
            return Response({"message": f"User with this email:{email} already exist"})

        new_user = User.objects.create(email=email, username=username, password=make_password(password))
        new_user.save()
    # return render(request, "estate/register.html")
    return Response({"Status": "SignUp has been successfully"})



class AnnounceAPIView(APIView):
    
    def get(self, request):
        return Response({'header': 'Private house'})


    def post(self, request):
        new_announce = Announcement.objects.create(
            header = request.data['header'],
            text = request.data['text'],
            author_id = request.data['author_id']
        )

        return Response({'announce': model_to_dict(new_announce)}, 200)