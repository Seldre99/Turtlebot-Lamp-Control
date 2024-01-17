#!/usr/bin/env python

import rospy
from my_turtlebot_project.msg import LightBulbStatus


def see_message(data):
    rospy.loginfo(data.status + ": " + str(data.touched) + " è stata accesa")


if __name__ == '__main__':
    try:
        rospy.init_node('message_received_node', anonymous=True)
        rospy.Subscriber('/custom_message', LightBulbStatus, see_message, queue_size=1)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass