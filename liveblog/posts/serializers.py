
from rest_framework.serializers import ModelSerializer

from .models import Liveblog


class LiveblogSerializer(ModelSerializer):
    class Meta:
        model = Liveblog
        fields = ('id', 'title')
        read_only_fields = ('slug', )
