from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:form_id>/', views.detail, name='detail'),
    path('<int:form_id>/results/', views.results, name='results'),
    path('<str:form_id>/load/', views.load, name='load'),
]

