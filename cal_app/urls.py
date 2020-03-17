from django.conf.urls import url
from django.urls import path
from . import views as core_views

app_name = 'cal_app'
urlpatterns = [
    url(r'^index/$', core_views.index, name='index'),
    url(r'^calendar/$', core_views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', core_views.new, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', core_views.edit, name='event_edit'),
    url(r'^event/delete/(?P<event_id>\d+)/$', core_views.delete, name='delete'),
    url(r'^signup/$', core_views.signup, name='signup'),
]
