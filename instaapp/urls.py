from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.welcome, name="welcome"),
    # url(r'^picture',views.picture, name ='picture'),
    url(r'^newpicture$',views.new_picture, name ='new_picture'),
    url(r'^profile$', views.user_profile, name='user-profile'),
    url(r'^editprofile$', views.edit_profile, name="edit-profile"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^newcomment/(\d+)/$', views.new_comment, name='new-comment'),
    url(r'^likes/(?P<id>\d+)',  views.likes, name='like')


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)