#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from tf.transformations import euler_from_quaternion, quaternion_from_euler

twist = Twist()
#imu_topic: "/imu_data"
low_speed=-4
high_speed=4
low_turn= -2
high_turn= 2
step_size= 0.01

def get_rotation (msg):
    print("in get")
    global prev_yaw, prev_pitch

    
    orientation_q = msg.orientation
    (yaw, pitch, roll)  = [orientation_q.x, orientation_q.y, orientation_q.z]
    #print("roll: ", roll, "pitch: ", pitch, "yaw: ", yaw)

    Send_Twist(yaw,pitch,roll)

def Send_Twist(yaw,pitch,roll):

    control_speed = 0
    control_turn = 0

    yaw = int(yaw)
    pitch = int(pitch)
    roll = int(roll)
    print("roll: ", roll, "pitch: ", pitch, "yaw: ", yaw)
    
    if(yaw>-80 and yaw<25):
        if(pitch<5 and pitch >-2):
            if(roll<3 and roll > -2):
                control_speed = 0 
                control_turn = 0 
            else:
                control_speed = 0
                control_turn = roll* 0.05
        else:
            control_speed = pitch * 0.01
            control_turn = 0

        
    else:
        print("Stabilize your Hand")

    print("control_speed", control_speed)
    print("control_turn", control_turn)
    
    twist.linear.x = control_speed; 
    twist.linear.y = 0;
    twist.linear.z = 0
    twist.angular.x = 0; 
    twist.angular.y = 0; 
    twist.angular.z= control_turn
    
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    pub.publish(twist)
    
    rate = rospy.Rate(10) # 10hz
    rate.sleep()

rospy.init_node('my_quaternion_to_euler')
sub = rospy.Subscriber ('/imu_data', Imu, get_rotation, queue_size=1)

r = rospy.Rate(1)

while not rospy.is_shutdown():
    r.sleep()