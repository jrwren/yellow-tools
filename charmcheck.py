#!/usr/bin/python
"""
Check for the charm on our many different sites.

Usage:   charmcheck.py charm-id
Example: charmcheck.py "~bac/xenial/charmworld"
"""

from pprint import pprint
import requests
import sys


CS = 'https://api.{server}jujucharms.com/charmstore/v5/{{charmid}}/meta/id'
CW = 'http://manage.jujucharms.com/api/3/charm/{charmid}'
LEGACY = 'https://store.juju.ubuntu.com/charm-info?charms=cs:{charmid}'

servers = (
    ('Legacy', LEGACY),
    ('Charmworld', CW),
    ('Staging', CS.format(server='staging.')),
    ('Production', CS.format(server='')),
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
    for servername, template in servers:
        url = template.format(charmid=charmid)
        print_banner(servername)
        get_response(url)


if __name__ == '__main__':
   main(sys.argv[1])
