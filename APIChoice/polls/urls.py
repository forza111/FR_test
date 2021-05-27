from django.urls import path
from . import views,admin

urlpatterns = ([
    path("survey/", views.SurveyViewSet.as_view({'get': 'list'})),
    path("survey/<int:pk>", views.SurveyViewSet.as_view({'get': 'retrieve'})),
    path("createquestionnaire/", views.SurveyViewSet.as_view({'post':'create'})),
    path("questionnaire/", views.QuestionnaireDetailView.as_view({'get': 'list'})),
    path("questionnaire/<int:pk>", views.QuestionnaireDetailView.as_view({'get': 'retrieve'})),
    path("createanswer/<int:pk>", views.AnswerCreateViewSet.as_view({'patch': 'partial_update'})),
    path("admin/survey/", admin.AdminSurveyViewSet.as_view({'get': 'list'})),
    path("admin/createsurvey/", admin.AdminSurveyViewSet.as_view({'post': 'create'})),
    path("admin/change_survey/<int:pk>", admin.AdminSurveyViewSet.as_view({'patch': 'partial_update',
                                                                           "get":"retrieve",
                                                                           "delete": "destroy"})),
    path("admin/questions/", admin.AdminQuestionViewSet.as_view({'get': 'list'})),
    path("admin/createquestion/", admin.AdminQuestionViewSet.as_view({'post': 'create'})),
])
