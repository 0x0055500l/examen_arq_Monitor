from django.urls import path
from . import views

app_name = "sistema"

urlpatterns = [
    path('', views.index, name='index'),
    path('api/metrics/', views.api_metrics, name='api_metrics'),
]
