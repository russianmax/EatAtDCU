from django.urls import path

from . import views

app_name = 'eatatdcu'

urlpatterns = [
    path('', views.index, name='index'),
]
