#!/bin/sh
while [ 1 ]; do
    python pullAndSend.py &
    sleep 15
done
