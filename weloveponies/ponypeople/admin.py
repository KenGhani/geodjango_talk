from django.contrib import admin
from django.contrib.gis import admin
from models import *

class CountyAdmin(admin.OSMGeoAdmin):
    #list_display = ['name10', 'state__name10']
    #list_filter = ['state__name10']
    search_fields = ['name10']

admin.site.register(Djangonaut, admin.OSMGeoAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(State, admin.OSMGeoAdmin)