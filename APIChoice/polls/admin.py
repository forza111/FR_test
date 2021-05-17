from django.contrib import admin
from .models import Survey, Question, Choice, TypeQuestion, Questionnaire, Answer

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(TypeQuestion)
admin.site.register(Questionnaire)
admin.site.register(Answer)



# Register your models here.
