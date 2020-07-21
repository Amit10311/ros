#! /usr/bin/env python

import math, rospy
from utilities import set_model_state, get_model_state, \
                      spawn_coke_can, spawn_table, \
                      pause_physics, unpause_physics
from geometry_msgs.msg import Pose, Point, Quaternion

from tf.transformations import quaternion_from_euler


rospy.init_node('euler')

# RPY to convert: 90deg, 0, -90deg
q = quaternion_from_euler(math.radians(90), 0, math.radians(-90))
Quaternion(*q)
rospy.loginfo(Quaternion(*q))
