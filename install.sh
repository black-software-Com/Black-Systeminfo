#!/bin/sh
# Black-Systeminfo
if [[ "$(id -u)" -ne 0 ]];
then
  echo "Please, Run This Program as Root!"
  exit
fi
function main() {
    printf '\033]2;Black-Systeminfo/Installing\a'
    clear
    echo "Installing..."
    chmod a+x black.py
    sleep 2
    apt install python
    apt install python3
    apt install python3-pip
    pip3 install --upgrade pip
    sleep 0.50
    echo "
Finish...

Usage:
     python black.py
     "
    exit
}
main