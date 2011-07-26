from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'people/view_people.html'}),
    url(r'^people/$', 'ponypeople.views.get_djangonauts', name="get_djangonauts"),
    url(r'^counties/$', 'ponypeople.views.get_counties', name="get_counties"),
    #url(r'schools/(?P<school_year>\d{4})/list/(?P<list_slug>[-\w]+)/$', 'school_rankings.views.list_page', name='school_rankings_list'),
)
