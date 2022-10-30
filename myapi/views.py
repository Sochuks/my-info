from rest_framework import viewsets
from .serializers import DetailsSerializer
from .models import Details

from django.shortcuts import render


class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all().order_by('slackUsername')
    serializer_class = DetailsSerializer
