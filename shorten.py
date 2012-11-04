#!/usr/bin/env python

import sys, subprocess

if len(sys.argv) <= 1 :
  print 'Usage: shorten credential_file url [code]'
  print 'Credential file must contain username:password for HTTP authorization'
  exit(1)

credential_file = sys.argv[1]
url = sys.argv[2]
code = sys.argv[3] if len(sys.argv) >= 4 else None

host='https://patrickhay.es'
#host='localhost:5000'

username_and_password = open(credential_file).readlines()[0].strip()

command = ['curl',
  '-k', # Because heroku owns my SSL cert
  '-s', # silent
  '-i', # Include HTTP headers in output (so we can get the shortened response)
  '-F', 'url=' + url,  # post data
  '-u', username_and_password,  # http basic auth
  host + '/shorten',
  ]
if code :
  command.extend(['-F', 'code=' + code])

output = subprocess.check_output(command)

success = False
for line in output.split('\n') :
  if line.startswith('Location:' ) :
    success = True
    print line[len('Location: '):].replace('patrickhay.es', 'phay.es')
    exit(0)

if not success :
  print output
  exit(1)
