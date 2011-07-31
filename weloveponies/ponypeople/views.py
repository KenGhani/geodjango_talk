import json
import colorsys

from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.contrib.gis.measure import Distance

from models import Djangonaut, State

def get_people(request):
    people = []
    for person in Djangonaut.objects.all():
        people.append({
            'id': person.id,
            'name': person.name,
            'geojson': person.location.geojson,
        })

    return HttpResponse(
        json.dumps({'people': people}),
        mimetype="application/json"
    )


def get_people_nearby(request, djangonaut_id):
    person = get_object_or_404(Djangonaut, pk=djangonaut_id)
    people = []
    for person in Djangonaut.objects.exclude(id=djangonaut_id).filter(location__distance_lt=(person.location, Distance(mi=5))):
        people.append(person.name)

    return HttpResponse(
        json.dumps({'people': people}),
        mimetype='application/json',
    )

def get_states(request):
    states = []
    min_people = 99999999999999999
    max_people = -1

    for state in State.objects.annotate(Count('djangonauts')):
        min_people = min(state.djangonauts__count, min_people)
        max_people = max(state.djangonauts__count, max_people)

        states.append({
            'name': state.name10,
            'num_people': state.djangonauts__count,
            'geojson_boundry': state.geom.geojson,
            'geojson_center': state.geom.centroid.geojson
        })

    for state in states:
        state['color'] = generate_shade(min_people, max_people, state['num_people'])

    return HttpResponse(
        json.dumps({'states': states}),
        mimetype='application/json',
    )

# ==========================================================================================

def generate_shade(min, max, value):
    color = colorsys.rgb_to_hls(204/255, 255/255, 240/255)
    max_lightness = 0.95
    min_lightness = 0.05
    color_step = (max_lightness-min_lightness)/(max-min)
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
