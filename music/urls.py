
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
               #/music/
               url(r'^$', views.index, name='index'),
               #/music/login
               url(r'^login/$', views.Userform.as_view(), name='userform'),
               #/music/66/
               url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),
               #/music/66/favorite
               url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
               #/music/album/add/
               url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

                #/music/album/66/
               url(r'^album/(?P<album_id>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

               #/music/album/66/delete
               url(r'^album/(?P<album_id>[0-9]+)/delete$', views.AlbumDelete.as_view(), name='album-delete'),

               #/music/contact
              url(r'^contact/$', views.contact, name='contact'),
              #music/logout
              url(r'^logout/$', views.logout_user, name='logout_user'),
]
