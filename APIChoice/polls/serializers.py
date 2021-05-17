from rest_framework import serializers
from .models import Survey, Questionnaire, Answer

class SurveyListSerializer(serializers.ModelSerializer):
    '''Список активных опросов'''

    class Meta:
        model = Survey
        fields = "__all__"


class QuestionnaireCreateSerializer(serializers.ModelSerializer):
    '''Создание опросного листа'''

    class Meta:
        model = Questionnaire
        fields = "__all__"

class AnswerCreateSerializer(serializers.ModelSerializer):
    '''Заполнение ответов'''

    class Meta:
        model = Answer
        fields = "__all__"