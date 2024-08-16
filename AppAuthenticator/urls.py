from django.urls import path
from . import views

urlpatterns = [
    path('', views.requestPage, name="request_page"),
    path('error/', views.errorPage, name="error_page"),
    path('response/', views.responsePage, name="response_page")
]