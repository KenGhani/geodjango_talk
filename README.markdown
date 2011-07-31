Source Code for WeLovePonies:  A GeoDjango talk by Eric Palakovich Carr
=======================================================================

This repository hosts the end result of my GeoDjango talk.  Currently, this is the source code that was made during
my talk on July 27th, 2011 (http://www.meetup.com/django-district/events/16015696/).  Later, this will host the source
code of the online version of my talk.

You can view the slides on slideshare:

http://www.slideshare.net/bigsassy/geotalk-presentation-8738796

INSTALLATION (apologies for lack of detail):
--------------------------------------------

### Install PostGIS using GeoDjango documentation
https://docs.djangoproject.com/en/1.3/ref/contrib/gis/install/

### Create the weloveponies database

    CREATE DATABASE weloveponies WITH TEMPLATE template_postgis;

### Clone this repository

    $ git clone git://github.com/bigsassy/geodjango_talk.git

### Create the virtualenv in the geodjango_talk directory

    $ cd geodjango_talk
    $ virtualenv --no-site-packages virenv
    $ source virenv/bin/activate
    $ pip -E virenv install -r REQUIREMENTS

### Update the settings.py to include you database information

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'weloveponies',
            'USER': '<your user name>',
            'PASSWORD': '<your password>',
        }
    }

### Sync the DB

    $ cd weloveponies
    $ python manage.py syncdb

### Load the data
    $ python manage.py shell
    >>> execfile('../data/load_data.py')

Try it out:
-----------

1.  Run the runserver command
2.  Take a look at people at http://localhost:8000/ponypeople/people/
3.  Take a look at the states visualization at http://localhost:8000/ponypeople/states/

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