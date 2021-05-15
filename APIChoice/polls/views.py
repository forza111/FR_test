from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Survey
from .serializers import SurveyListSerializer
from datetime import datetime

class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    '''Список  активных опросов'''

    def get_queryset(self):
        surveys = Survey.objects.filter(
            beginning_date__lte=datetime.now()).filter(
            completion_date__gte=datetime.now()
        )
        return surveys
    serializer_class = SurveyListSerializer