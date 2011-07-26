# Code for loading people.p.  Run in manage.py shell

import cPickle
from ponypeople.models import Djangonaut
from django.contrib.gis.geos import Point

people = cPickle.loads(open('../data/people.p', 'r').read())

for person in people:
    Djangonaut.objects.create(
        name=person[2],
        location=Point(person[1], person[0])
    )
