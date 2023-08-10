from rest_framework import serializers
from .models import Indice
from .models import PIB

class IndiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indice
        exclude = ['id']

class PIBSerializer(serializers.ModelSerializer):
    class Meta:
        model = PIB
        exclude = ['id']
