#!/bin/bash

ZPOOL_FILE="/tmp/zpool.statusfile"
FS_FILE="/tmp/filesystem.statusfile"
BLK_FILE="/tmp/block.statusfile"

sudo rm /tmp/*.statusfile

while [ 1 ]; do

	date              >  $ZPOOL_FILE
	echo -e "\n"      >> $ZPOOL_FILE
	sudo zpool list   >> $ZPOOL_FILE
	echo -e "\n"      >> $ZPOOL_FILE
	sudo zpool iostat >> $ZPOOL_FILE
	echo -e "\n"      >> $ZPOOL_FILE
	sudo zpool status >> $ZPOOL_FILE

	df -hT > $FS_FILE

	lsblk -i   >  $BLK_FILE
	echo       >> $BLK_FILE
	sudo blkid >> $BLK_FILE

	sleep 5m

done
