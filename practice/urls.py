from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("thank-you/", views.index, name='thank-you')
]
