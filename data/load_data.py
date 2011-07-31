import os
import sys
import cPickle

from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point

from ponypeople.models import Djangonaut, State, state_mapping

# Load the States
data_path = os.path.abspath('../data/tl_2010_us_state10')

lm = LayerMapping(State, data_path, state_mapping, transform=False, encoding='iso-8859-1')
lm.save(strict=True, verbose=True)

# Load the people
print 'Loading people...'
people = cPickle.loads(open('../data/people.p', 'r').read())

for person in people:
    Djangonaut.objects.create(
        name=person[2],
        location=Point(person[1], person[0])
    )
