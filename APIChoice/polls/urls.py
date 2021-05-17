from django.urls import path
from . import views

urlpatterns = ([
    path("survey/", views.SurveyViewSet.as_view({'get': 'list'})),
    path("createqn/", views.QuestionnaireCreateViewSet.as_view({'post':'create'})),
    path("createans/<int:pk>", views.AnswerCreateViewSet.as_view({'post': 'create'})),
])
