#!/bin/bash

sudo pkill monitor.sh
sudo service apache2 restart
./app/monitor.sh &
