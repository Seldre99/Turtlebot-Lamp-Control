#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from gazebo_msgs.msg import ModelStates

def model_states_callback(data):
    rospy.Rate(1)
    contact_pub = rospy.Publisher('/contact_status', String, queue_size=10)
 
    # Estrai la coordinata y del modello 'lampadina'
    index_lamp1 = data.name.index('lampadina')
    y_coordinate_lamp1 = data.pose[index_lamp1].position.y
    
    # Estrai la coordinata y del modello 'lampadina_2'
    index_lamp2 = data.name.index('lampadina_2')
    y_coordinate_lamp2 = data.pose[index_lamp2].position.y
    
    # Estrai la coordinata y del modello 'lampadina_3'
    index_lamp3 = data.name.index('lampadina_3')
    y_coordinate_lamp3 = data.pose[index_lamp3].position.y
    
    # Estrai la coordinata y del modello 'turtlebot3_burger'
    index_turtle = data.name.index('turtlebot3_burger')
    y_coordinate_turtle = data.pose[index_turtle].position.y
    
    # Simula la lettura del sensore di contatto
    # e pubblica lo stato sul topic /contact_status
    if abs(y_coordinate_lamp1 - y_coordinate_turtle) <= 0.01: 
        contact_status = "contatto rilevato con lampadina 1"
        contact_pub.publish(contact_status)
    elif abs(y_coordinate_lamp2 - y_coordinate_turtle) <= 0.01:
        contact_status = "contatto rilevato con lampadina 2"
        contact_pub.publish(contact_status)
    elif abs(y_coordinate_lamp3 - y_coordinate_turtle) <= 0.01:
        contact_status = "contatto rilevato con lampadina 3"
        contact_pub.publish(contact_status)

       
def contact_sensor():
    rospy.init_node('contact_sensor_node', anonymous=True)
    rospy.Subscriber('/gazebo/model_states', ModelStates, model_states_callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        contact_sensor()
    except rospy.ROSInterruptException:
        pass
