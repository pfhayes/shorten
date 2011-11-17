#/usr/bin/python

import sys, subprocess

if len(sys.argv) <= 1 :
  print 'Usage: shorten url [code]'
  exit(1)

url = sys.argv[1]
code = sys.argv[2] if len(sys.argv) >= 3 else None

command = ['curl', '-s', '-i', 'http://patrickhay.es/shorten', '-F', 'url=' + url]
if code :
  command.extend(['-F', 'code=' + code])

output = subprocess.check_output(command)

success = False
for line in output.split('\n') :
  if line.startswith('Location:' ) :
    success = True
    print line[len('Location: '):]
    exit(0)

if not success :
  print output
  exit(1)
