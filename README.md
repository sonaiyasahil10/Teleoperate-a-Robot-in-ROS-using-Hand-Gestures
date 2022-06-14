# Teleoperate-a-Robot-in-ROS-using-Hand-Gestures

P.S: Have reffered to Lentin Joseph Sir's "ROS ROBOTICS PROJECT" book for this project

Aim: To teleoperate a custom bot (Guido) using hand gestures

Pre-requisite: Have ROS and Rosserial set up on your PC/Laptop

Hardware used: Arduino Mega
               IMU MPU-6050
               Jumper Cables
      
Connections:

Arduino code:

Plug your Arduino and run the following commands:
* To view imu_frame
1) $ roscore
2) $ rosrun rosserial_python serial_node.py /dev/ttyACM0 (the port where Arduino is connected)
3) check if the topic "imu_data" and "tf" is availabe using the command: $ rostopic list
4) $ rosrun rviz rviz -f base_link (Add tf topic in rviz window for 

* To control a bot in gazebo 

$ rosrun gesture_teleop triaimu_controller_ypr.py 
$ roslaunch guido_sim_description gazebo.launch 

Working:

Final Product
