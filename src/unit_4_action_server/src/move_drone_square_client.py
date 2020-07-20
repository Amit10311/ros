#! /usr/bin/env python
import rospy
import time
import actionlib

from actionlib.msg import TestFeedback, TestResult, TestAction, TestGoal
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

nImage = 1

def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

# initializes the action client node
rospy.init_node('drone_action_move_client')

# create the connection to the action server
client = actionlib.SimpleActionClient('/move_drone_square_as', TestAction)
# waits until the action server is up and running
client.wait_for_server()

# creates a goal to send to the action server
goal = TestGoal()
goal.goal= 5 

# indicates, take pictures along 10 seconds


# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)

# Uncomment these lines to test goal preemption:
#time.sleep(3.0)
#client.cancel_goal()  # would cancel the goal 3 seconds after starting

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time 
# status = client.get_state()
# check the client API link below for more info

client.wait_for_result()

print('[Result] State: %d'%(client.get_state()))