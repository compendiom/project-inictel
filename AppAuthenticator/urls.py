from django.urls import path
from . import views

urlpatterns = [
    path('', views.requestPage, name="request page"),
    path('error/', views.errorPage, name="error page"),
    path('response/', views.responsePage, name="response page")
]