#!/bin/bash
trap ctrl_c INT

if [ -z "$1" ]
then
	iteration=50
else
	iteration=$1
fi

function ctrl_c(){
    echo "** Trapped CTRL-C"
    exit
}

for ((i=1; i < $iteration; i++))
do 
	#top -l 1 -s 2 | grep Python | awk {'print $1, $2, $3'}
	#count=`top -l 1 -stats pid,command,cpu | grep Python | wc -l`
	#top -l 2 -stats pid,command,cpu | grep Python | tail -n $count
	txt=`top -l 2 -stats pid,command,cpu | grep Python`
	total=`echo "$txt" | wc -l`
	count=`expr $total / 2`
	echo "$txt" | tail -n $count
	echo "----------------------"
done
