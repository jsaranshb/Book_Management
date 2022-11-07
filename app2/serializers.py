from rest_framework.serializers import ModelSerializer
from .models import new_one

class NewSerializer(ModelSerializer):
    class Meta:
        model = new_one
        fields = '__all__'