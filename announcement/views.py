from django.shortcuts import render
from .models import Announcement
from rest_framework.views import APIView
from rest_framework import serializers
from .serializers import AnnounceSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class AnnounceAPIView(APIView):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return render(request, 'announce.html')


    def post(self, request):
        user_id = request.user.id
        serializer = AnnounceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        new_announce = Announcement.objects.create(
            header = data['header'],
            text = data['text'],
            author_id = user_id
        )
        new_announce.save()

        return Response({"announce": serializer.data}, 200)
    

class UpdateAnnounceApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self,request, author_id):
        user_id = request.user.id
        serializer = AnnounceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        header = data['header']
        text = data['text']

        announce = Announcement.objects.get(author_id=user_id)
        if not announce:
            return Response({"error": "This announce does not exist. Method PUT not allowed"})
         
        announce.header = data['header']
        announce.text = data['text']      
        
        announce.save()
        return Response({"new_announce": serializer.data}, 200)
        
    
class DeleteAnnounceApiView(AnnounceAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, author_id):
        user_id = request.user.id
        announce = Announcement.objects.filter(author_id=user_id).first()
        announce.delete()

        return Response({"Announce": "Was Deleted"})


