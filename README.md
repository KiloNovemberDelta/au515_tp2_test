# IPSA : TP2 Visual Servoing
### Create your environment

First, if you do not have the catwin_ws folder, create it : 

`mkdir -p ~/catkin_ws/src`

Then go to this folder, and copy the project : 

`cd ~/catkin_ws/src`

`git clone https://github.com/KiloNovemberDelta/au515_tp2_test`

Go inside, and run the installation script (only once !) for OpenCV : 

`cd ~/catkin_ws/src/au515_tp2_test`

`./install_opencv3.sh`

When the script has finished, source the bashrc : 

`source ~/.bashrc` 

Finally compile the project : 

`cd ~/catkin_ws`

`catkin_make au515_tp2_test`

`source ~/catkin_ws/devel/setup.bash` 



### Run the code

To run the code with the runner and the follower : 

`roslaunch au515_tp2_test test.launch`