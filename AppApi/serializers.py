from rest_framework import serializers
from AppApi.models import VideoInfo 

class VideoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoInfo
        fields="__all__"