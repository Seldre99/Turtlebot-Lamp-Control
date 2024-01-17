#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import ModelStates
from my_turtlebot_project.srv import ControlLightBulb, ControlLightBulbResponse

# Dichiarazione delle variabili globali per le posizioni delle lampadine
lamp1_position = None
lamp2_position = None
lamp3_position = None

def model_states_callback(data):
    global lamp1_position, lamp2_position, lamp3_position
    try:
        lamp1_index = data.name.index('lampadina')
        lamp1_position = data.pose[lamp1_index].position.x
    except ValueError:
        lamp1_position = None

    try:
        lamp2_index = data.name.index('lampadina_2')
        lamp2_position = data.pose[lamp2_index].position.x
    except ValueError:
        lamp2_position = None

    try:
        lamp3_index = data.name.index('lampadina_3')
        lamp3_position = data.pose[lamp3_index].position.x
    except ValueError:
        lamp3_position = None

def response(data):
    global lamp1_position, lamp2_position, lamp3_position

    if data.command == "lampadina":
        if lamp1_position == 7.0:
            resp = "Lampadina 1 accesa"
        else:
            resp = "Lampadina 1 spenta"
    elif data.command == "lampadina_2":
        if lamp2_position == 7.0:
            resp = "Lampadina 2 accesa"
        else:
            resp = "Lampadina 2 spenta"
    elif data.command == "lampadina_3":
        if lamp3_position == 7.0:
            resp = "Lampadina 3 accesa"
        else:
            resp = "Lampadina 3 spenta"

    return ControlLightBulbResponse(resp)

def check_on_server():
    rospy.init_node('check_server')
    rospy.Subscriber('/gazebo/model_states', ModelStates, model_states_callback)
    rospy.Service('check_on', ControlLightBulb, response)
    print("Pronto a dire lo stato delle lampadine")
    rospy.spin()

if __name__ == "__main__":
    check_on_server()
