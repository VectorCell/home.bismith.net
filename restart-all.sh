#!/bin/bash

sudo pkill monitor.sh
sudo service apache2 restart
./monitor.sh &
