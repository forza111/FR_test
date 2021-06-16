from django.urls import path
from . import views,admin
from APIChoice.yasg import urlpatterns as doc_urls

urlpatterns = ([
    path("survey/", views.SurveyViewSet.as_view({'get': 'list'})),
    path("survey/<int:pk>", views.SurveyViewSet.as_view({'get': 'retrieve'})),
    path("create_questionnaire/", views.SurveyViewSet.as_view({'post':'create'})),
    path("questionnaire/", views.QuestionnaireDetailView.as_view({'get': 'list'})),
    path("questionnaire/<int:pk>", views.QuestionnaireDetailView.as_view({'get': 'retrieve'})),
    path("create_answer/<int:pk>", views.AnswerCreateViewSet.as_view({'patch': 'partial_update',
                                                                      "get":"retrieve",})),
    path("admin/survey/", admin.AdminSurveyViewSet.as_view({'get': 'list'})),
    path("admin/create_survey/", admin.AdminSurveyCreate.as_view({'post': 'create'})),
    path("admin/change_survey/<int:pk>", admin.AdminSurveyViewSet.as_view({'patch': 'partial_update',
                                                                           "get":"retrieve",
                                                                           "delete": "destroy"})),
    path("admin/questions/", admin.AdminQuestionViewSet.as_view({'get': 'list'})),
    path("admin/create_question/", admin.AdminQuestionViewSet.as_view({'post': 'create'})),
    path("admin/change_question/<int:pk>", admin.AdminQuestionViewSet.as_view({'patch': 'partial_update',
                                                                                "get":"retrieve",
                                                                                "delete": "destroy"})),
    path("admin/choices/", admin.AdminChoiceViewSet.as_view({'get': 'list'})),
    path("admin/create_choice/", admin.AdminChoiceViewSet.as_view({'post': 'create'})),
    path("admin/change_choice/<int:pk>", admin.AdminChoiceViewSet.as_view({'patch': 'partial_update',
                                                                           "get":"retrieve",
                                                                           "delete": "destroy"})),
])


urlpatterns += doc_urls