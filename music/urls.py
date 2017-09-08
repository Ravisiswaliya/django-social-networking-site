from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name = 'home'),
    url(r'^(?P<pk>\d+)/', views.DetailView.as_view(), name='detail'),
    url(r'^album/add/$', views.CreateView.as_view(), name='album-add'),
    url(r'^album/(?P<pk>\d+)/update/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'^album/(?P<pk>\d+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^song/(?P<pk>\d+)/delete/$', views.SongDelete.as_view(), name='song-delete'),
]