from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<recipe_id>[0-9]+)/ingredients/$', views.ingredients, name='ingredients'),
    url(r'^(?P<recipe_id>[0-9]+)/instructions/$', views.instructions, name='instructions'),
    url(r'^(?P<recipe_id>[0-9]+)/ingredients/edit/$', views.ingredient_edit, name='edit_ingredients'),
    url(r'^(?P<recipe_id>[0-9]+)/instructions/edit/$', views.instruction_edit, name='edit_instructions'),
    url(r'^(?P<recipe_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),
]
