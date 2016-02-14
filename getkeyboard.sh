#!/bin/bash
# most hackish way to get the path to keyboard
echo "/dev/input/event"`xinput | grep "Virtual core keyboard" | tail -c 24 | head -c 1`
