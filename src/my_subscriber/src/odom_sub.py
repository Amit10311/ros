#! /usr/bin/env python

import rospy                                          
from nav_msgs.msg import Odometry


def callback(msg):                        # 1. Define a function called 'callback' that receives a parameter 
                                          
 
    print msg.header                        


rospy.init_node('odom_subscriber')          # 2. Initiate a Node called 'topic_subscriber'

                                          
sub = rospy.Subscriber('/odom', Odometry, callback)   
             
                  
rospy.spin() 