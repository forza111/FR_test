from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Survey,Answer
from .serializers import SurveyListSerializer, QuestionnaireCreateSerializer, AnswerCreateSerializer, SurveyDetailSerializer
from datetime import datetime

class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    '''Список  активных опросов'''

    def get_queryset(self):
        """surveys = Survey.objects.filter(
            beginning_date__lte=datetime.now()).filter(
            completion_date__gte=datetime.now()
        )"""
        surveys = Survey.objects.all()
        return surveys

    def get_serializer_class(self):
        if self.action == "list":
            return SurveyListSerializer
        elif self.action == "retrieve":
            return SurveyDetailSerializer

class QuestionnaireCreateViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        surveys = Survey.objects.filter(
            beginning_date__lte=datetime.now()).filter(
            completion_date__gte=datetime.now()
        )
        return surveys
    serializer_class = QuestionnaireCreateSerializer



#class QuestionnaireDetailView(viewsets.ModelViewSet):



class AnswerCreateViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        answers = Answer.objects.get()
        return answers
    serializer_class = AnswerCreateSerializer



