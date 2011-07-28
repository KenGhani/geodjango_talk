import colorsys
import math
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Count
import json

from models import Djangonaut, County, State

def get_djangonauts(request):
    people = []

    for person in Djangonaut.objects.all():
        people.append({
            'name': person.name,
            'geojson': person.location.geojson,
        })

    return HttpResponse(
        json.dumps({'people': people}),
        mimetype="application/json"
    )

def get_states(request):
    states = []

    min_people = None
    max_people = None

    # Get the base statistics
    for state in State.objects.all():
        num_djangonauts = Djangonaut.objects.filter(location__within=state.geom).count()

        if num_djangonauts > 0:
            if min_people is None or min_people > num_djangonauts:
                min_people = num_djangonauts
            if max_people is None or max_people < num_djangonauts:
                max_people = num_djangonauts

            states.append({
                'id': state.id,
                'name': state.name10,
                'num_djangonauts': num_djangonauts,
                'geojson_boundries': state.geom.geojson,
                'geojson_center': state.geom.centroid.geojson
            })

    # Get the color for each state
    for state_info in states:
        state_info['color'] = generate_shade(min_people, max_people, state_info['num_djangonauts'])

    # Create json, inserting each person's geojson coordinates after converting dict into json
    return HttpResponse(
        json.dumps({'states': states}),
        mimetype="application/json"
    )

def get_people_in_state(request, state_id):
    state = get_object_or_404(State, pk=state_id)
    people = []
    
    for person in Djangonaut.objects.filter(location__within=state.geom):
        people.append({
            'geojson': person.location.geojson,
        })

    return HttpResponse(
        json.dumps({'people': people}),
        mimetype="application/json"
    )

def generate_shade(min, max, value):
    color = colorsys.rgb_to_hls(204/255, 255/255, 240/255)
    max_lightness = 0.95 #
    min_lightness = 0.05
    color_step = (max_lightness-min_lightness)/(max-min) # go from brighter light (0.95) to pretty dark (0.05)
    return rgb_to_color_string(colorsys.hls_to_rgb(color[0], (max_lightness - (value * color_step)) + min_lightness, color[2]))

def rgb_to_color_string(rgb):
    """
    Turns a 3 tuple of 0-255 RGB values into a hexadecimal color string:
    Ex:  (255,0,255) turns into #FF00FF
    """
    r = ('%x' % int(rgb[0] * 255)).zfill(2)
    g = ('%x' % int(rgb[1] * 255)).zfill(2)
    b = ('%x' % int(rgb[2] * 255)).zfill(2)

    return "#%s%s%s" % (r,g,b)