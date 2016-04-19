#!/bin/bash

# Check the status on many microservices.
# Usage: jujucharmstatus.sh [domain]
# If domain is blank then production is used.

set -eux
if [[ -z "$@" ]]; then
    domain="jujucharms.com"
else
    domain="$1.jujucharms.com"
fi
   
http https://$domain/_version
http https://api.$domain/identity/v1/debug/info
http https://demo.$domain/version
http https://api.$domain/charmstore/debug/info
http https://api.$domain/charmstore/v4/debug/status
