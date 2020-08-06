#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist 

rospy.init_node('topic_publisher')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
count = Twist()
count.linear = 0
count.angular = 0 

while not rospy.is_shutdown(): 
  pub.publish(count)
  count.linear=0.5
  count.angular=0.5
  rate.sleep()