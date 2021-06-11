from django.contrib import admin
from .models import Survey, Question, Choice, TypeQuestion, Questionnaire, Answer
from rest_framework import viewsets
from .serializers import SurveyListSerializer, SurveyCreateSerializer,\
    SurveyDetailSerializer, QuestionForAnswerSerializer, ChoiceListSerializer
from rest_framework import permissions,authentication

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(TypeQuestion)
admin.site.register(Questionnaire)
admin.site.register(Answer)



class AdminModelViewSet(viewsets.ModelViewSet):
    '''Вью класс для администратора'''
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]


class AdminSurveyViewSet(AdminModelViewSet):
    '''Опросы'''
    queryset = Survey.objects.all()
    serializer_class = SurveyCreateSerializer


class AdminSurveyDetailViewSet(AdminModelViewSet):
    '''Подробная информация опроса'''
    queryset = Survey.objects.all()
    serializer_class = SurveyDetailSerializer


class AdminQuestionViewSet(AdminModelViewSet):
    '''Вопросы'''
    queryset = Question.objects.all()
    serializer_class = QuestionForAnswerSerializer


class AdminChoiceViewSet(AdminModelViewSet):
    '''Варианты ответа на вопросы'''
    queryset = Choice.objects.all()
    serializer_class = ChoiceListSerializer


