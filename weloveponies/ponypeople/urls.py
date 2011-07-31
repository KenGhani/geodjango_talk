from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^people/$', direct_to_template, {'template': 'ponypeople/view_people.html'}),
    url(r'^people/json/$', 'ponypeople.views.get_people', name="get_people"),
    url(r'^people/(?P<djangonaut_id>\d+)/json/$', 'ponypeople.views.get_people_nearby', name="get_people_nearby"),
    url(r'^states/$', direct_to_template, {'template': 'ponypeople/view_states.html'}),
    url(r'^states/json/$', 'ponypeople.views.get_states', name="get_states"),
)
  