import os
from django.contrib.gis.utils import LayerMapping
from ponypeople.models import *

# States
data_path = os.path.abspath('../data/tl_2010_us_state10')
lm = LayerMapping(State, data_path, state_mapping, transform=False, encoding='iso-8859-1')
lm.save(strict=True, verbose=True)

# Counties
data_path = os.path.abspath('../data/tl_2010_us_county10')
lm = LayerMapping(County, data_path, county_mapping, transform=False, encoding='iso-8859-1')
lm.save(strict=True, verbose=True)

# Link the counties with their states using a foreign key
from django.db import connection, transaction
cursor = connection.cursor()
cursor.execute("""
    UPDATE ponypeople_county AS c
    SET c.state_id=s.id
    FROM ponypeople_state AS s
    WHERE c.statefp10=s.statefp10;
""")
transaction.commit_unless_managed()
