from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.contrib.gis.db import models

class Djangonaut(models.Model):

    name = models.CharField(max_length=500)
    location = models.PointField()
    state = models.ForeignKey('ponypeople.State', null=True, related_name='djangonauts')

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

@receiver(pre_save, sender=Djangonaut)
def djangonaut_save_handler(sender, **kwargs):
    try:
        djangonaut = kwargs['instance']
        djangonaut.state = State.objects.get(geom__contains=djangonaut.location)
    except:
        pass

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