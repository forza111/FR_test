from django.contrib import admin
from .models import Survey, Question, Choice, TypeQuestion, Questionnaire, Answer
from rest_framework import viewsets
from .serializers import SurveyListSerializer, \
    AnswerCreateSerializer, SurveyDetailSerializer, QuestionnaireDetailSerializer, \
    QuestionnaireListSerializer,QuestionnaireCreateSerializer
from rest_framework import permissions,authentication

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(TypeQuestion)
admin.site.register(Questionnaire)
admin.site.register(Answer)



class AdminModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]


class AdminSurveyViewSet(AdminModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveyListSerializer