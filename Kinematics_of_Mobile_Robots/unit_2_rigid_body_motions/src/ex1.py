#! /usr/bin/env python

import math, rospy
from utilities import set_model_state, get_model_state, \
                      spawn_coke_can, spawn_table, \
                      pause_physics, unpause_physics
from geometry_msgs.msg import Pose, Point, Quaternion

x, y, z = 1, 0, 0
for angle in range(0,360,10):
    theta = math.radians(angle)
    xp = x * math.cos(theta) - y * math.sin(theta)
    yp = x * math.sin(theta) + y * math.cos(theta)
    set_model_state('coke_can', Pose(position=Point(xp,yp,z)))
    rospy.sleep(0.1)