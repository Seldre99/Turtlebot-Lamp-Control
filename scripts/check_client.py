#!/usr/bin/env python

import rospy
import sys
from my_turtlebot_project.srv import ControlLightBulb


def status(command):
    rospy.wait_for_service("check_on")
    try:
        request = rospy.ServiceProxy('check_on', ControlLightBulb)
        response = request(command)
        return response.risposta
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            command = str(sys.argv[1])
            print("Richiesto stato di %s" %command)
            print(status(command))
    except rospy.ROSInterruptException:
        pass