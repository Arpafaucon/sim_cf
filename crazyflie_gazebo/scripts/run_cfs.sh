#!/bin/bash

cf_gazebo_location=$(rospack find crazyflie_gazebo)

# Resolve script location using :
# https://stackoverflow.com/a/246128/7002298
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
runcfs_dir="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
echo "script location is $runcfs_dir"

cf2=$runcfs_dir/../../crazyflie-firmware/sitl_make/build/cf2

if [ -z "$1" ]
then
	max_cfs=1
else
	if [ $1 -gt 4 ]
	then
		echo "WARNING: allocating more than 4 crazyflies to the same port is not recommended."
		echo "Split crazyflie swarm into groups of 4 on different ports if you experience issues"
		read -n1 -r -p "Press any key to continue..."
	fi
	max_cfs=$1
fi

if [ -z "$2" ]
then
	udp_port=19950
else
	udp_port=$2
fi

if [ -z "$3" ]
then
	ip_address=INADDR_ANY
else
	ip_address=$3
fi

counter=1
while [ $counter -le $max_cfs ]
do
	$cf2 $counter $udp_port $ip_address &
	sleep 0.3
	((counter++))
done