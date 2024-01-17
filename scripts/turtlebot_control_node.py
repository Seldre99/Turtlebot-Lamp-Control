#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def contact_callback(contact_msg):
    if contact_msg.data == "contatto rilevato con lampadina 1":
        rospy.set_param("lampadina", 1)
        rospy.loginfo("Contatto rilevato! Accendiamo la lampadina 1.")
    elif contact_msg.data == "contatto rilevato con lampadina 2":
        rospy.set_param("lampadina", 2)
        rospy.loginfo("Contatto rilevato! Accendiamo la lampadina 2.")
    elif contact_msg.data == "contatto rilevato con lampadina 3":
        rospy.set_param("lampadina", 3)
        rospy.loginfo("Contatto rilevato! Accendiamo la lampadina 3.")
    else:
        rospy.loginfo("Nessun contatto.")


if __name__ == '__main__':
    rospy.init_node('turtlebot_control_node', anonymous=True)
    rate = rospy.Rate(1)
    rospy.Subscriber('/contact_status', String, contact_callback)
    
    while not rospy.is_shutdown():
        try:
            rate.sleep()
        except rospy.ROSInterruptException:
            pass
