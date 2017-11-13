from django.conf.urls import url
from .views import RecipeCreate, RecipeUpdate

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', RecipeCreate.as_view(template_name="recipes/recipe_edit.html"), name='add'),
    url(r'^(?P<pk>[0-9]+)/edit/$', RecipeUpdate.as_view(template_name="recipes/recipe_edit.html"), name='edit'),
    url(r'^(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),
]
