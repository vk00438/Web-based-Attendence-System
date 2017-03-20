from django.conf.urls import url
from . import views
#this app_name is to distinguish same urls for two apps
app_name = 'employee'


urlpatterns = [
    # for /index/
    url(r'^$', views.index, name='home'),
    # for /about/
    url(r'^about/$', views.about, name='about'),
    # for /dashboard/
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    # for /settings/
    url(r'^settings/$', views.settings, name='settings'),

    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^header/$', views.showip, name='showip')
]