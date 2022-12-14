from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name="PersonalDetails"),
    path('empwork',views.empwork,name="WorkDetails"),
    path('qualify',views.qualify,name="Qualification"),
    path('finish',views.finish,name="finish")
]
