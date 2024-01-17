#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import keyboard

def move_turtlebot3():
    rospy.init_node('move_turtlebot3_node', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    move_cmd = Twist()
    linear_speed = 0.5  # Velocità lineare
    angular_speed = 0.5  # Velocità angolare

    while not rospy.is_shutdown():
        if keyboard.is_pressed('w'):
            move_cmd.linear.x = linear_speed  # Avanti
            move_cmd.angular.z = 0.0
        elif keyboard.is_pressed('s'):
            move_cmd.linear.x = -linear_speed  # Indietro
            move_cmd.angular.z = 0.0
        elif keyboard.is_pressed('a'):
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = angular_speed  # Sinistra
        elif keyboard.is_pressed('d'):
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = -angular_speed  # Destra
        else:
            move_cmd.linear.x = 0.0  # Fermarsi
            move_cmd.angular.z = 0.0
        
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtlebot3()
    except rospy.ROSInterruptException:
        pass