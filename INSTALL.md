# Install Notes
starting from ubuntu 18.04, with ros mininmal
installed
```sh
sudo apt install protobuf-compiler libgo
sudo apt install ros-melodic-mav-comm ros-melodic-joy
git clone https://github.com/wuwushrek/sim_cf.git 
git submodule update --init --recursive
pip3 install rospkg catkin_pkg --user
catkin build -DPYTHON_EXECUTABLE=/usr/bin/python3
sudo apt install libopencv-dev
sudo apt install ros-melodic-cv-bridge
```