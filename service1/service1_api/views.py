from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response

from rest_framework.views import APIView
from .models import Basic_metals
from .serializers import Basic_metalSerializer

class GetDataAPIView(APIView):

    def get(self, request):
        data = Basic_metals.objects.all()        
        serializer = Basic_metalSerializer(data, many=True)
        return Response(serializer.data)

class GetDataDetailedAPIView(APIView):
    def get(self,request,pk):
        data = Basic_metals.objects.filter(category=pk)
        serializer = Basic_metalSerializer(data, many=True)
        return Response(serializer.data)

