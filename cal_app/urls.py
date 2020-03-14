from django.conf.urls import url
from . import views

app_name = 'cal_app'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.new, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.edit, name='event_edit'),
    url(r'^event/delete/(?P<event_id>\d+)/$', views.delete, name='delete'),
]
