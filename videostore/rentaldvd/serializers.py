from .models import Dvd
from rest_framework import routers, serializers, viewsets

class DvdApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dvd
        fields = ('id', 'user', 'title', 'content', 'status', 'date_took', 'date_returned', )