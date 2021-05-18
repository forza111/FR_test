from django.urls import path
from . import views

urlpatterns = ([
    path("survey/", views.SurveyViewSet.as_view({'get': 'list'})),
    path("survey/<int:pk>", views.SurveyViewSet.as_view({'get': 'retrieve'})),
    path("createquestionnaire/", views.QuestionnaireCreateViewSet.as_view({'post':'create'})),
    path("createans/<int:pk>", views.AnswerCreateViewSet.as_view({'post': 'create'})),
])
