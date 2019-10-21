from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.welcome, name="welcome"),
    url(r'^picture',views.picture, name ='picture'),
    url(r'^new/picture',views.new_picture, name ='new-picture'),
    url(r'^profile/(\d+)', views.user_profile, name='user-profile'),
    url(r'^editprofile$', views.edit_profile, name="edit-profile"),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^follow/(\d+)',views.follow, name='follow'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)