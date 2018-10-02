from django.conf.urls import url

from . import views
app_name = 'eatatdcu'
urlpatterns = [
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^restaurants/', views.restaurants, name='restaurants'),
=======
    url(r'^restaurants$', views.restaurants, name='restaurants'),
>>>>>>> upstream/master
]
