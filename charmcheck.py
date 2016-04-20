#!/usr/bin/python
"""
Check for the charm on our many different sites.

Usage:   charmcheck.py charm-id
Example: charmcheck.py "~bac/xenial/charmworld"
"""

from pprint import pprint
import requests
import sys


CS = 'https://api.{server}{domain}/charmstore/v5/{{charmid}}/meta/id'
CW = 'http://manage.jujucharms.com/api/3/charm/{charmid}'
LEGACY = 'https://store.juju.ubuntu.com/charm-info?charms=cs:{charmid}'

servers = (
    ('Legacy', (LEGACY, )),
    ('Charmworld', (CW, )),
    ('GUI MAAS', (
        CS.format(server='', domain='jujugui.org').replace('https', 'http'),
        CS.format(server='', domain='jujugui.org').replace('https', 'http').replace('meta/id','meta/extra-info'))),
    ('Staging', (
        CS.format(server='staging.', domain='jujucharms.com'),
        CS.format(server='staging.', domain='jujucharms.com').replace('meta/id','meta/extra-info'))),
    ('Production', (
        CS.format(server='', domain='jujucharms.com'),
        CS.format(server='', domain='jujucharms.com').replace('meta/id','meta/extra-info'))),
)

def get_response(url):
    resp = requests.get(url)
    if not resp.ok:
        print "NOT FOUND: {}".format(url)
    else:
        pprint(resp.json())
    print

def print_banner(name):
    marker = "-" * len(name)
    print marker
    print name
    print marker

def main(charmid):
    for servername, templates in servers:
        for template in templates:
            url = template.format(charmid=charmid)
            print_banner(servername)
            try:
                get_response(url)
            except requests.exceptions.ConnectionError:
                print url
                raise


if __name__ == '__main__':
   charmid = sys.argv[1]
   if charmid.startswith('cs:'):
       charmid = charmid[3:]
   main(charmid)
