from django.urls import path
from . import views

urlpatterns = ([
    path("survey/", views.SurveyViewSet.as_view({'get': 'list'}))
])
