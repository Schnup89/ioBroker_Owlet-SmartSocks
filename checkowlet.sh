#!/bin/sh

if ! ps -ef | grep owletio.py | grep -v grep; then
  echo "$(date) --- Python3 (owlet) not found!" >> /tmp/OwletWatchdog
  /usr/bin/python3 /etc/scripts/owletio.py &
fi
