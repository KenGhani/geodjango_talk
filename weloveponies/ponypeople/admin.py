from django.contrib.gis import admin
from models import Djangonaut, State

admin.site.register(Djangonaut, admin.OSMGeoAdmin)
admin.site.register(State, admin.OSMGeoAdmin)
