#! /usr/bin/env python

import rospy                                          
from sensor_msgs.msg import LaserScan

def callback(msg):                        # 1. Define a function called 'callback' that receives a parameter 
                                          
 
    print msg.ranges[360]                       


rospy.init_node('laser_subscriber')          # 2. Initiate a Node called 'topic_subscriber'

                                          
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)   
             
                  
rospy.spin() 