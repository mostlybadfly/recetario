from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
import recipes.views

urlpatterns = [
    url(r'^$', recipes.views.index),
    url(r'^recipes/', include('recipes.urls')),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', recipes.views.signup, name='signup'),
]
