#!/bin/bash
while 'true'; do
    python3 -c "import sys; print(sys.path)"
    python3 /home/pyrrhus/enphase2influx/pullAndSend.py &
    sleep 15
done
