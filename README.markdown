Source Code for WeLovePonies:  A GeoDjango talk by Eric Palakovich Carr
=======================================================================

This repository hosts the end result of my GeoDjango talk.  Currently, this is the source code that was made during
my talk on July 27th, 2011 (http://www.meetup.com/django-district/events/16015696/).  Later, this will host the source
code of the online version of my talk.

INSTALLATION (apologies for lack of detail):
--------------------------------------------

1.  Install PostGIS using GeoDjango documentation:  https://docs.djangoproject.com/en/1.3/ref/contrib/gis/install/
2.  Create the weloveponies database
        CREATE DATABASE weloveponies WITH TEMPLATE template_postgis;
3.  Clone this repository
        ~/source$ git clone git://github.com/bigsassy/geodjango_talk.git
        ~/source$ cd geodjango_talk
4.  Create the virtualenv in the base directory
        geodjango_talk$ virtualenv --no-site-packages virenv
        geodjango_talk$ source virenv/bin/activate
        geodjango_talk$ pip -E virenv install -r REQUIREMENTS
5.  Update the settings.py to include you database information
        DATABASES = {
            'default': {
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': 'weloveponies',
                'USER': '<your user name>',
                'PASSWORD': '<your password>',
            }
        }
6.  Sync the DB
        geodjango_talk$ cd weloveponies
        weloveponies$ python manage.py syncdb
7.  Load the data
        weloveponies$ python manage.py shell
        # in shell
        In [1]: execfile('../data/load_data.py')

IMPORTANT NOTE:
---------------

At this point the talk and code is a little incomplete.  The biggest issue would be the incredibly large size of the
JSON data for the states (about 22MB).  Future versions of the talk will discuss techniques to solve this problem
(generating custom map tiles, Douglas–Peucker algorithm, etc).

In the meantime, if you want a simplified version of the states you can use the XML feed from this page:

http://econym.org.uk/gmap/example_states.htm

The feed is here:

http://econym.org.uk/gmap/states.xml

A person at the talk I gave provided the link to me, but I'm ashamed to say I've already forgotten who exactly that
person was.  If you're reading this, drop me a message here on github so I can give you my thanks publicly in this
README :)