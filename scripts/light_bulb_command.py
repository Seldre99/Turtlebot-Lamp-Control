#!/usr/bin/env python

import rospy
from gazebo_msgs.msg import ModelStates, ModelState 
from gazebo_msgs.srv import SetModelState
from my_turtlebot_project.msg import LightBulbStatus 


def check_command(data):
    set_coordinate_x = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
    lamp = rospy.get_param("lampadina")
    light_message = rospy.Publisher('/custom_message', LightBulbStatus, queue_size=10)
    model_state = ModelState()
    msg = LightBulbStatus()
    if lamp == 1:
        model_state.model_name = 'lampadina'
        model_state.pose.position.x = 7
        model_state.pose.position.y = data.pose[data.name.index('lampadina')].position.y
        set_coordinate_x(model_state)
        msg.status = "Lampadina 1"
        msg.touched = True
        light_message.publish(msg)
    elif lamp == 2:
        model_state.model_name = 'lampadina_2'
        model_state.pose.position.x = 7
        model_state.pose.position.y = data.pose[data.name.index('lampadina_2')].position.y
        set_coordinate_x(model_state)
        msg.status = "Lampadina 2"
        msg.touched = True
        light_message.publish(msg)
    elif lamp == 3:
        model_state.model_name = 'lampadina_3'
        model_state.pose.position.x = 7
        model_state.pose.position.y = data.pose[data.name.index('lampadina_3')].position.y
        set_coordinate_x(model_state)
        msg.status = "Lampadina 3"
        msg.touched = True
        light_message.publish(msg)
    
    


if __name__ == '__main__':
    try:
        rospy.init_node('check_command_node', anonymous=True)
        rospy.Subscriber('/gazebo/model_states', ModelStates, check_command)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass