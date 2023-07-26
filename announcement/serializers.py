from rest_framework import serializers
from .models import Announcement

class AnnounceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = (
            'header',
            'text'
        )