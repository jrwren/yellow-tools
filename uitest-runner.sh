#!/bin/bash

set -eux

# Create $HOME/.uitest-creds with:

#credentials=LPUSERNAME:LPPASSWORD
#admin=admin:ADMINPASSWORD

. $HOME/.uitest-creds

case $1 in
    production)
	url='https://jujucharms.com'
	;;
    staging)
	url='https://staging.jujucharms.com'
	;;
    *)
	url='https://www.jujugui.org'
	;;
esac

devenv/bin/uitest  --url $url --credentials $credentials --admin $admin -c lxd --debug $2
