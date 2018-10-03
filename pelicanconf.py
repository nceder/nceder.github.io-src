#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Naomi Ceder'
SITENAME = 'Naomi Ceder'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = 'pelican-alchemy/alchemy'

# Blogroll
LINKS = (('Training', 'https://training.naomiceder.tech'),
        ( 'Speaking', '/speaking/'),
        ('Talks', '/talks/'),
        ('Python Software Foundation', 'https://www.python.org/psf'),
        ('Python.org', 'http://python.org/'),
        )

# Social widget
SOCIAL = (( 'LinkedIn', 'https://www.linkedin.com/in/naomiceder'),
          ('Twitter', '@NaomiCeder'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
