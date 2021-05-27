from rest_framework import serializers
from .models import Survey, Questionnaire, Answer, Question, Choice


class ChoiceListSerializer(serializers.ModelSerializer):
    '''Варианты выбора'''
    class Meta:
        model = Choice
        fields = ["number_choice", "choice_text"]


class QuestionDetailSerializer(serializers.ModelSerializer):

    type_question = serializers.SlugRelatedField(slug_field="title", read_only=True)
    choices = ChoiceListSerializer(many=True)

    class Meta:
        model = Question
        fields = ["number_question","question_text","type_question", "choices"]


class SurveyDetailSerializer(serializers.ModelSerializer):
    '''Подробная информация о опросе'''
    quest = QuestionDetailSerializer(many=True)

    class Meta:
        model = Survey
        fields = "__all__"



class SurveyListSerializer(serializers.ModelSerializer):
    '''Список активных опросов'''

    class Meta:
        model = Survey
        fields = "__all__"
        read_only_fields = ("beginning_date",)


class QuestionnaireListSerializer(serializers.ModelSerializer):
    '''Вывод списка опросных листов'''
    survey = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Questionnaire
        fields = "__all__"


class QuestionnaireCreateSerializer(serializers.ModelSerializer):
    '''Создание опросного листа'''

    class Meta:
        model = Questionnaire
        fields = "__all__"


class QuestionDetailForAnswerSerializer(serializers.ModelSerializer):
    '''Вопросы для опросника'''
    choices = ChoiceListSerializer(many=True)
    type_question = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Question
        fields = ["number_question","question_text", "type_question", "choices"]


class AnswerDetailSerializer(serializers.ModelSerializer):
    '''Ответы на вопросы'''
    question = QuestionDetailForAnswerSerializer()
    class Meta:
        model = Answer
        fields = ["question", "answer"]


class QuestionForAnswerSerializer(serializers.ModelSerializer):
    '''Сериалиизатор для ответов'''
    class Meta:
        model = Question
        fields = '__all__'


class AnswerCreateSerializer(serializers.ModelSerializer):
    '''Написание ответов на вопросы'''
    question = QuestionDetailForAnswerSerializer(read_only=True)

    '''def validate_answer(self,value):
        if Answer.objects.filter(question.type_question.title == "Выбор"):
            if '1' not in value:
                raise serializers.ValidationError("")
            return value'''

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionnaireDetailSerializer(serializers.ModelSerializer):
    '''Информация об опросном листе'''
    survey = serializers.SlugRelatedField(slug_field="title", read_only=True)
    ans = AnswerDetailSerializer(many=True)

    class Meta:
        model = Questionnaire
        fields = ["id","user_id", "survey", "ans"]



class AnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'

    def validate_ans(self,value):
         if Answer.objects.get(pk=...).question.type_question.title == "Выбор":
            if '1' not in value:
                raise serializers.ValidationError("Ошибка")
            return value
