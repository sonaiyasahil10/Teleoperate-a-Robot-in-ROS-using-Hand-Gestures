# Teleoperate-a-Robot-in-ROS-using-Hand-Gestures

P.S: Have reffered to Lentin Joseph Sir's ***"ROS ROBOTICS PROJECT"*** book for this project.

**Pre-requisite: Have ROS and Rosserial set up on your PC/Laptop.**

## Hardware used: 
- Arduino Mega
- IMU MPU-6050 (for MPU 9 series you can refer to the book directly)
- Jumper Cables
      
## Connections:

## Arduino:

1) Launch Arduino IDE and Install MPU-6050 libraray
2) Compile and Upload _mpu6050_ros_ypr.ino_

### To view imu_frame
Plug in your Arduino and run the following commands

1) $ roscore
2) $ rosrun rosserial_python serial_node.py /dev/ttyACM0 (the port where Arduino is connected)
3) check if the topic "imu_data" and "tf" is availabe using the command: $ rostopic list
4) $ rosrun rviz rviz -f base_link (Add tf topic in rviz window for 

### To control a bot in gazebo 
1. $ roscore
2. $ rosrun rosserial_python serial_node.py /dev/ttyACM0 (the port where Arduino is connected)
3. $ rosrun gesture_teleop ***imu_controller_ypr.py***
4. $ roslaunch guido_sim_description gazebo.launch (or any your custom made bot) 

## Working:

## Final Product
