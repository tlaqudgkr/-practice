from django.conf.urls import url, include
from django.contrib import admin

from .views import HomeView, UserRegisterView, UserRegisterDoneView, myGamePlay

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserRegisterView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserRegisterDoneView.as_view(), name='register_done'),
    url(r'^admin/', admin.site.urls),

    url(r'^mygame/', include('mygame.urls', namespace='mygame')),
    url(r'^ajax/mygame/detail/', myGamePlay, name='ajaxmygameplay')
]
