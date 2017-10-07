from django.conf.urls import include, url
from django.contrib import admin
import recipes.views

urlpatterns = [
    url(r'^$', recipes.views.index),
    url(r'^recipes', include('recipes.urls')),
    url(r'^admin/', admin.site.urls),
]
