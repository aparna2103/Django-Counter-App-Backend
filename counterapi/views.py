from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import CounterSerializer
from .models import Counter
from rest_framework.response import Response
from rest_framework import status
import json


class CounterViewSet(viewsets.ModelViewSet):
    queryset = Counter.objects.all().order_by('name')
    serializer_class = CounterSerializer

    def create(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        data =json.loads(request.body)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
