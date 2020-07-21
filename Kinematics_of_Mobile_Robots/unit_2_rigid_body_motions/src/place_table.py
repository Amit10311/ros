#! /usr/bin/env python

import math, rospy
from utilities import set_model_state
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_about_axis, quaternion_multiply

position = Point(1,0,0)
q = quaternion_about_axis(math.radians(90), (0,0,1))
orientation = Quaternion(*q)
set_model_state('table', Pose(position, orientation))