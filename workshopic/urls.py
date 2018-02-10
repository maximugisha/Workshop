from django.conf.urls import url
from . import views
#add a url pattern to point to a view
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^reg_page$', views.reg_page, name='reg_page'),
    url(r'^attendants$', views.attendants, name='attendants'),
    url(r'^participant/(?P<pk>\d+)/$', views.participant_detail, name='participant_detail'),
    url(r'^search$', views.search, name='search'),
    url(r'^participant/new/$', views.new_participant, name='new_participant'),
]