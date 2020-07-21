#! /usr/bin/env python

import math, rospy
from utilities import set_model_state, get_model_state, \
                      spawn_coke_can, spawn_table, \
                      pause_physics, unpause_physics
from geometry_msgs.msg import Pose, Point, Quaternion

from tf.transformations import quaternion_from_euler

rospy.init_node('euler2')

position = Point(x=0.5, y=0, z=0.5)
roll, pitch, yaw = 90, 0, -90

q_rpy = quaternion_from_euler(math.radians(roll), math.radians(pitch), math.radians(yaw))
orientation = Quaternion(*q_rpy)
set_model_state('coke_can', Pose(position, orientation))
orientation

rospy.loginfo(orientation)
