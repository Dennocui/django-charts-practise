from chartjs import views 
from django.urls import path

app_name = "chartjs"

urlpatterns = [

    path('', views.HomeView, name="charts"),
]