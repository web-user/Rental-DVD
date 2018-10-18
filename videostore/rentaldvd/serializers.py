from .models import Dvd
from rest_framework import routers, serializers, viewsets

class DvdApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dvd
        fields = ('id', 'title', 'content',)