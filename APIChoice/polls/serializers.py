from rest_framework import serializers
from .models import Survey

class SurveyListSerializer(serializers.ModelSerializer):
    '''Список активных опросов'''

    class Meta:
        model = Survey
        fields = "__all__"