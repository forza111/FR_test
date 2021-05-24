from django.urls import path
from . import views

urlpatterns = ([
    path("survey/", views.SurveyViewSet.as_view({'get': 'list'})),
    path("survey/<int:pk>", views.SurveyViewSet.as_view({'get': 'retrieve'})),
    path("createquestionnaire/", views.SurveyViewSet.as_view({'post':'create'})),
    path("questionnaire/", views.QuestionnaireDetailView.as_view({'get': 'list'})),
    path("questionnaire/<int:pk>", views.QuestionnaireDetailView.as_view({'get': 'retrieve'})),
    path("createanswer/<int:pk>", views.AnswerCreateViewSet.as_view({'patch': 'partial_update'})),
])
