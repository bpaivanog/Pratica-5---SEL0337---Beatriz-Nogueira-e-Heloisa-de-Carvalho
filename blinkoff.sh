#!/bin/bash
# blinkoff.sh

GPIO=18
if [-d/sys/class/gpio/gpio$GPIO]; then
	echo 0 > sys/class/gpio/gpio$GPIO/value
	echo $GPIO > sys/class/gpio/unexport
fi
