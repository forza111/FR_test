from django.contrib import admin
from .models import Survey, Question, Choice, TypeQuestion

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(TypeQuestion)


# Register your models here.
