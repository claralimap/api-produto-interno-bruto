from django.shortcuts import render
from rest_framework import viewsets
from .models import Indice
from .serializers import IndiceSerializer

from .models import PIB
from .serializers import PIBSerializer

from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView



class IndiceFilter(filters.FilterSet):
    
    class Meta:
        model = Indice
        fields = {
            'ano': ['icontains'],
            'mes': ['iexact']
        }
class IndiceViewSet(viewsets.ModelViewSet):
    queryset = Indice.objects.all().order_by('ano')
    serializer_class = IndiceSerializer
    pagination_class = LimitOffsetPagination #?limit=2 por exemplo (numero de itens por pagina)
    filterset_class = IndiceFilter
    
    
class MyView(APIView):
    permission_classes = [IsAuthenticated]


class PIBViewSet(viewsets.ModelViewSet):
    queryset = PIB.objects.all()
    serializer_class = PIBSerializer

class PIBFilter(filters.FilterSet):
    
    class Meta:
        model = PIB
        fields = {
            'ano': ['icontains'],
            'id_uf': ['iexact']
        }

class PIBViewSet(viewsets.ModelViewSet):
    queryset = PIB.objects.all().order_by('ano')
    serializer_class = PIBSerializer
    pagination_class = LimitOffsetPagination 
    filterset_class = PIBFilter   