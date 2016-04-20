# yellow-tools

A collection of little scripts that make developing for jujucharms.com easier.

[charmcheck.py](charmcheck.py)
------------------------------

Checks the status of a charm-id across the many systems we care about: legacy
charmstore, charmworld, staging charmstore, and production charmstore.

Usage:
`charmcheck.py charm-id`

Example:
`charmcheck.py "~bac/precise/charmworld"

[jujucharms-status.sh](jujucharms-status.sh)
--------------------------------------------

Checks the status information across many microservices.

Usage:
`jujucharms-status.sh` (checks production)

`jujucharms-status.sh staging` (checks staging)

Requirements:
[httpie](https://pypi.python.org/pypi/httpie)
