#!/bin/sh
while [ 1 ]; do
    python /home/pyrrhus/enphase2influx/pullAndSend.py &
    sleep 15
done
