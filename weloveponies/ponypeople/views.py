from annoying.decorators import ajax_request
from django.db.models import Count

from models import Djangonaut, County, State

@ajax_request
def get_djangonauts(request):
    people = []
    for person in Djangonaut.objects.all():
        people.append({
            'name': person.name,
            'lng': person.location.coords[0],
            'lat': person.location.coords[1],
        })
    return { 'people': people }

@ajax_request
def get_counties(request):
    counties = []
    
    for county in County.objects.all():
        counties.append({
            'name': county.name10,
            'num_djangonauts': Djangonaut.objects.filter(location__within=county.geom).count()
        })

    return { 'counties': counties }

def generate_ethnic_breakdown_data(ethnic_breakdown):
    """
    Figures out the color to represent each enthnicity in the graph, starting by giving the smallest
    minority the lightest color and getting progressively darker with each larger race.  Also
    calculates the width of the divs for the graph on the webpage.
    """
    lightest_color = colorsys.rgb_to_hls(1, 215.0/255, 153.0/255)
    colors = [colorsys.hls_to_rgb(lightest_color[0], lightest_color[1] - (0.08*i), lightest_color[2])
              for i in range(len(ethnic_breakdown))]
    sorted_ethnicities_min_to_maj = sorted(ethnic_breakdown.iteritems(), key=operator.itemgetter(1))
    total_points = float(sum([v for v in ethnic_breakdown.values()]))
    total_div_width = 400 # pixels
    remaining_width = total_div_width

    color_breakdown = []
    for i,color in enumerate(colors):
        width = math.floor(total_div_width * (sorted_ethnicities_min_to_maj[i][1]/total_points))
        remaining_width -= width
        color_breakdown.append({
            'label': sorted_ethnicities_min_to_maj[i][0],
            'percentage': sorted_ethnicities_min_to_maj[i][1] * 100,
            'color': rgb_to_color_string(color),
            'width': width
        })
    if remaining_width > 0:
        color_breakdown[-1]['width'] += remaining_width

    return list(reversed(color_breakdown)) # this will return the list in the order it will be rendered

def rgb_to_color_string(rgb):
    """
    Turns a 3 tuple of 0-255 RGB values into a hexadecimal color string:
    Ex:  (255,0,255) turns into #FF00FF
    """
    r = ('%x' % int(rgb[0] * 255)).zfill(2)
    g = ('%x' % int(rgb[1] * 255)).zfill(2)
    b = ('%x' % int(rgb[2] * 255)).zfill(2)

    return "#%s%s%s" % (r,g,b)