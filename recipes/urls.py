from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<recipe_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),
]
