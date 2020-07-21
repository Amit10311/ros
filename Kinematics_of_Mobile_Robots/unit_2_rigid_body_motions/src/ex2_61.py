#! /usr/bin/env python

import math, rospy
from utilities import set_model_state, get_model_state, \
                      spawn_coke_can, spawn_table, \
                      pause_physics, unpause_physics
from geometry_msgs.msg import Pose, Point, Quaternion

from tf.transformations import quaternion_from_euler

rospy.init_node('euler1')

# RPY to convert: 40deg, 0, -40deg

q = quaternion_from_euler(math.radians(40), 0, math.radians(-40))
Quaternion(*q)

rospy.loginfo(Quaternion(*q))


# roll, pitch, yaw = 40, 0, -40