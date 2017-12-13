from django.urls import path

from . import views

app_name = 'loaders'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:form_id>/', views.detail, name='detail'),
    path('<int:form_id>/results/', views.results, name='results'),
    path('<str:form_id>/load/', views.load, name='load'),
]

