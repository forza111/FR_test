from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Survey,Answer, Questionnaire
from .serializers import SurveyListSerializer, \
    AnswerCreateSerializer, SurveyDetailSerializer, QuestionnaireDetailSerializer, \
    QuestionnaireListSerializer,QuestionnaireCreateSerializer
from datetime import datetime

class SurveyViewSet(viewsets.ModelViewSet):
    '''Список  активных опросов'''

    def get_queryset(self):
        surveys = Survey.objects.filter(
            beginning_date__lte=datetime.now()).filter(
            completion_date__gte=datetime.now()
        )
        return surveys

    def get_serializer_class(self):
        if self.action == "list":
            return SurveyListSerializer
        elif self.action == "retrieve":
            return SurveyDetailSerializer
        elif self.action == 'create':
            return QuestionnaireCreateSerializer



class QuestionnaireDetailView(viewsets.ModelViewSet):
    def get_queryset(self):
        questionnaire = Questionnaire.objects.all()
        return questionnaire

    def get_serializer_class(self):
        if self.action == "list":
            return QuestionnaireListSerializer
        elif self.action == "retrieve":
            return QuestionnaireDetailSerializer



class AnswerCreateViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        answers = Answer.objects.all()
        return answers
    serializer_class = AnswerCreateSerializer

    def put(self,request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)




