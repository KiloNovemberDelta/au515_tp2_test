#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python-catkin-tools python3-dev python3-pip
sudo pip3 install --upgrade pip
sudo pip3 install rospkg catkin_pkg matplotlib opencv-contrib-python numpy

echo "Generating right folders.."

if [[ $(lsb_release -rs) == "20.04" ]]; then # replace 8.04 by the number of release you want

       echo "20.04 Ubuntu detected. Noetic need no more installation for opencv. Simulation is ready."
       exit
fi
if [[ $(lsb_release -rs) == "18.04" ]]; then # replace 8.04 by the number of release you want

       echo "18.04 Ubuntu detected. Melodic OpenCV installation starting.."
else
       echo "Cannot detect 20.04 or 18.04 version. Installation stop here. Ask to your teacher for help."
fi



#Big reset in case of running again the script
sudo rm -r ~/catkin_build_ws

mkdir -p ~/catkin_build_ws && cd ~/catkin_build_ws

echo "Set right configuration for python3" 

catkin config -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so
catkin config --install
mkdir -p src
cd src

echo "Cloning right OpenCV bridge"

FOLDER=~/catkin_build_ws/src/vision_opencv
URL=https://github.com/ros-perception/vision_opencv.git

if [ ! -d "$FOLDER" ] ; then
	git clone -b melodic $URL
	cd ~/catkin_build_ws
	catkin build cv_bridge
	source ~/.bashrc
	#TODO : Check if ROS_PACKAGE_PATH already contains the source 
	if [[ "$ROS_PACKAGE_PATH" =~ (^|:)"/home/$USER/catkin_build_ws/install/share"(|/)(:|$) ]]; then
	    echo "Not changing sourcing in bashrc"
	else
	    sudo echo "source ~/catkin_build_ws/install/setup.bash" >> ~/.bashrc
	fi
        source install/setup.bash --extend

    
else
    echo "Already built"
fi


