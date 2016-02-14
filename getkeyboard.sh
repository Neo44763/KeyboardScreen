#!/bin/bash
echo "/dev/input/event"`xinput | grep "Virtual core keyboard" | tail -c 24 | head -c 1`
