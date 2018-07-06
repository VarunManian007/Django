from django.conf.urls import url,include
from . import views
app_name="music"
urlpatterns = [
    #/music/
    url (r'^$',views.index,name='index'),
    #url(r'^music/$', include('music.urls', namespace="music")),
    #/music/det/
    # url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
    #
    # url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
    # url(r'album/add/$',views.AlbumCreate,name='album-add')
    url(r'login/', views.login, name='login'),
url (r'signup/',views.signup,name='signup'),
url (r'shirt/',views.shirt,name='shirt'),
url (r'camera/',views.camera,name='camera'),
url (r'watch/',views.watch,name='watch'),
]