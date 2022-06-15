# Teleoperate-a-Robot-in-ROS-using-Hand-Gestures

P.S: I have reffered to Lentin Joseph Sir's ***"ROS ROBOTICS PROJECT"*** book for this project.

## Pre-requisite:
1) Have ROS and Rosserial set up on your PC/Laptop.
2) Install MPU-6050 library by _Electronic Cats_ in your Arduino IDE.

## Hardware used: 
- Arduino Mega
- IMU MPU-6050 (for MPU 9 series you can refer to the book directly)
- Jumper Cables
      
## Connections:
<!--- ![test](images/connection_1.jpg) -->
<p align = "center"> <img src="https://github.com/sonaiyasahil10/Teleoperate-a-Robot-in-ROS-using-Hand-Gestures/blob/main/images/connection_1.jpg"  width="650" height="500" > </p>

## Code:
Arduino code (***mpu6050_ros_ypr.ino***) in the script folder computes the orientation values from the IMU and send it to PC through the rosserial protocol.<br/>
These orientation values are recieved by PC as ROS topics (/tf, /imu_data,etc) and are converted into twist messages using a ROS node (***imu_controller_ypr.py***).<br/>
These twist messages are then published to  "/cmd_vel"  topic to operate the bot in Gazebo.

## Arduino: 


Compile and Upload _mpu6050_ros_ypr.ino_

### To view imu_frame in Rviz
Plug in your Arduino and run the following commands

1) $ roscore
2) $ rosrun rosserial_python serial_node.py /dev/ttyACM0 (the port where Arduino is connected)
3) check if the topic "imu_data" and "tf" is availabe using the command: $ rostopic list
4) $ rosrun rviz rviz -f base_link (Add tf topic in rviz window for 

### To control a bot in gazebo 
Plug in your Arduino and run the following commands

1. $ roscore
2. $ rosrun rosserial_python serial_node.py /dev/ttyACM0 (the port where Arduino is connected)
3. $ rosrun gesture_teleop ***imu_controller_ypr.py***
4. $ roslaunch guido_sim_description gazebo.launch (or any your custom made bot) 

## Working:
<p align = "center"> <img src="https://github.com/sonaiyasahil10/Teleoperate-a-Robot-in-ROS-using-Hand-Gestures/blob/main/images/Hand_orientation.jpg"  width="650" height="500" > </p>

<p align = "center"> Where the Roll about X Axis is responsible for Left and Right turn motion and <br/>
Pitch about Y axis produces front and back motion.</p>

## Final Product
<p align = "center"> <img src="https://github.com/sonaiyasahil10/Teleoperate-a-Robot-in-ROS-using-Hand-Gestures/blob/main/images/final.jpeg"  width="650" height="500" > </p>
<p align = "center"> <img src="https://github.com/sonaiyasahil10/Teleoperate-a-Robot-in-ROS-using-Hand-Gestures/blob/main/images/final.jpeg"  width="650" height="500" > </p>
