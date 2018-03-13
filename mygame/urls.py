from django.conf.urls import url
from mygame import views
urlpatterns = [
    url(r'^$', views.GameListView.as_view(), name='gamelist'),
    url(r'^detail/$', views.GameDetailView.as_view(), name='gamedetail')
]