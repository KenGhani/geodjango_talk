from django.contrib.gis.db import models
from django.contrib.gis.maps import google

# Create your models here.

class Djangonaut(models.Model):

    name = models.TextField()
    location = models.PointField()   # Note!
    
    objects = models.GeoManager() # Note!

    def __unicode__(self):
        return self.name

class State(models.Model):
    region10 = models.CharField(max_length=2)
    division10 = models.CharField(max_length=2)
    statefp10 = models.CharField(max_length=2)
    statens10 = models.CharField(max_length=8)
    geoid10 = models.CharField(max_length=2)
    stusps10 = models.CharField(max_length=2)
    name10 = models.CharField(max_length=100)
    lsad10 = models.CharField(max_length=2)
    mtfcc10 = models.CharField(max_length=5)
    funcstat10 = models.CharField(max_length=1)
    aland10 = models.FloatField()
    awater10 = models.FloatField()
    intptlat10 = models.CharField(max_length=11)
    intptlon10 = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name10

# Auto-generated `LayerMapping` dictionary for State model
state_mapping = {
    'region10' : 'REGION10',
    'division10' : 'DIVISION10',
    'statefp10' : 'STATEFP10',
    'statens10' : 'STATENS10',
    'geoid10' : 'GEOID10',
    'stusps10' : 'STUSPS10',
    'name10' : 'NAME10',
    'lsad10' : 'LSAD10',
    'mtfcc10' : 'MTFCC10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON',
}

class County(models.Model):

    state = models.ForeignKey(State, null=True)

    statefp10 = models.CharField(max_length=2)
    countyfp10 = models.CharField(max_length=3)
    countyns10 = models.CharField(max_length=8)
    geoid10 = models.CharField(max_length=5)
    name10 = models.CharField(max_length=100)
    namelsad10 = models.CharField(max_length=100)
    lsad10 = models.CharField(max_length=2)
    classfp10 = models.CharField(max_length=2)
    mtfcc10 = models.CharField(max_length=5)
    csafp10 = models.CharField(max_length=3)
    cbsafp10 = models.CharField(max_length=5)
    metdivfp10 = models.CharField(max_length=5)
    funcstat10 = models.CharField(max_length=1)
    aland10 = models.FloatField()
    awater10 = models.FloatField()
    intptlat10 = models.CharField(max_length=11)
    intptlon10 = models.CharField(max_length=12)
    geom = models.MultiPolygonField(srid=4269)
    
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name10

# Auto-generated `LayerMapping` dictionary for Counties model
county_mapping = {
    'statefp10' : 'STATEFP10',
    'countyfp10' : 'COUNTYFP10',
    'countyns10' : 'COUNTYNS10',
    'geoid10' : 'GEOID10',
    'name10' : 'NAME10',
    'namelsad10' : 'NAMELSAD10',
    'lsad10' : 'LSAD10',
    'classfp10' : 'CLASSFP10',
    'mtfcc10' : 'MTFCC10',
    'csafp10' : 'CSAFP10',
    'cbsafp10' : 'CBSAFP10',
    'metdivfp10' : 'METDIVFP10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'geom' : 'MULTIPOLYGON',
}
