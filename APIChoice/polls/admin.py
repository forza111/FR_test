from django.contrib import admin
from .models import Survey, Question, Choice, TypeQuestion, Questionnaire, Answer
from rest_framework import viewsets
from .serializers import SurveyListSerializer, SurveyCreateSerializer,\
    SurveyDetailSerializer, QuestionForAnswerSerializer, ChoiceListSerializer,\
    TypeQuestionViewSet

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


class AdminSurveyCreate(AdminModelViewSet):
    '''Создание Опроса'''
    queryset = Survey.objects.all()
    serializer_class = SurveyCreateSerializer

class AdminSurveyViewSet(AdminModelViewSet):
    '''Опрос'''
    queryset = Survey.objects.all()
    serializer_class = SurveyListSerializer


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

class AdminTypeQuestionViewSet(AdminModelViewSet):
    '''Тип вопроса'''
    queryset = TypeQuestion.objects.all()
    serializer_class = TypeQuestionViewSet
