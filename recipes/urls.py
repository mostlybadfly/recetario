from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<recipe_id>[0-9]+)/ingredients/$', views.ingredients, name='ingredients'),
    url(r'^(?P<recipe_id>[0-9]+)/ingredients/add/$', views.ingredient_add, name='ingredient_add'),
    url(r'^(?P<recipe_id>[0-9]+)/ingredients/(?P<ingredient_id>[0-9]+)/edit/$',
        views.ingredient_edit, name='ingredient_edit'),
    url(r'^(?P<recipe_id>[0-9]+)/instructions/$', views.instructions, name='instructions'),
    url(r'^(?P<recipe_id>[0-9]+)/instructions/add/$', views.instruction_add, name='instruction_add'),
    url(r'^(?P<recipe_id>[0-9]+)/instructions/(?P<instruction_id>[0-9]+)/edit/$', 
        views.instruction_edit, name='instruction_edit'),
    url(r'^(?P<recipe_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),
]
