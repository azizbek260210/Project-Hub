from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('our-team/', views.TeamList.as_view()),
    path('portfolio/', views.PortfolioList.as_view()),
    path('lists-of-vacancy/', views.VacancyList.as_view()),
    path('vacancy-detail/<int:pk>/', views.VacancyDetail.as_view()),
    path('send-resume/', views.create_vacancy_resume),
    path('write-message/', views.create_message),
]
