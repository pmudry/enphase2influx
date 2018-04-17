#!/bin/sh
while [ 1 ]; do
    python PollAndPushServer.py &
    sleep 15
done
