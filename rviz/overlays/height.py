#!/usr/bin/env python

from jsk_rviz_plugins.msg import OverlayText, OverlayMenu
from std_msgs.msg import ColorRGBA, Float32
import rospy
import math
import random
from geometry_msgs.msg import PoseStamped

#from geometry_msgs.msg import Twist


class Droneheight(object):
    def __init__(self):
        
        self.text_pub = rospy.Publisher("/text", OverlayText, queue_size=1)
        
        self.plot_value_pub = rospy.Publisher("/plot_value_sample", Float32, queue_size=1)
        self.plot_value_pub_y = rospy.Publisher("/plot_value_dist", Float32, queue_size=1)
        self.piechart_value_pub = rospy.Publisher("/piechart_value_sample", Float32, queue_size=1)
        self.menu_publisher = rospy.Publisher("/test_menu", OverlayMenu, queue_size=1)
        self.plot_value = 0
        self.plot_value_y = 0
        self.piechart_value = 0
        self.max_distance_from_object = 10.0
        
        self.subs = rospy.Subscriber("/odom_visualization/pose", PoseStamped, self.pose_callback)
        
        self.counter = 0
        self.rate = rospy.Rate(100)
        self.overlaytext = self.update_overlaytext()
        self.menu = self.update_overlay_menu()
        
        

    def pose_callback(self, msg):
        self.plot_value = msg.pose.position.x
        self.plot_value_y = msg.pose.position.y
        self.piechart_value = msg.pose.position.z

    def update_overlaytext(self, number=1.23, number2=1.23, number3=20):  
        
        
        
        text = OverlayText()

        text.width = 200
        text.height = 400
        text.left = 10
        text.top = 10
        text.text_size = 12
        text.line_width = 2
        text.font = "DejaVu Sans Mono"
        text.text = """x=  %s
        y= %s
        Height(z)= %s
        """ % (str(number), str(number2), str(number3))
        text.fg_color = ColorRGBA(0 / 255.0, 100.0 / 255, 0.0 / 255.0, 1.0)
        text.bg_color = ColorRGBA(0.0, 0.0, 0.0, 0.2)
        
        return text
    
    def update_overlay_textonly(self, new_text):
        self.overlaytext.text = new_text


    def update_overlay_menu(self):
        menu = OverlayMenu()
        menu.title = "HaroSystemMode"
        menu.menus = ["Sleep", "Searching", "MovingInCircles","Waiting"]
        
        menu.current_index = self.counter % len(menu.menus)
        return menu
        
    def update_overlay_menu_haro_tf(self):
        menu = OverlayMenu()
        menu.title = "HaroDistanceFromPerson"
        menu.menus = ["FarAway", "CloseBy", "Target", "OtherWayRound"]
        
        fraction = 10.0
        
        if self.piechart_value < (math.pi/fraction):
            if self.plot_value >= self.max_distance_from_object:
                index = 0
            elif self.plot_value >= (self.max_distance_from_object/ fraction) and self.plot_value < self.max_distance_from_object:
                index = 1
            elif self.plot_value < (self.max_distance_from_object/fraction):
                index = 2
            
        else:
            index = 3
            
        menu.current_index = index
            
        return menu

    def start_dummy_demo(self):
        
        while not rospy.is_shutdown():
            self.overlaytext = self.update_overlaytext()
            self.menu = self.update_overlay_menu()
            
            if self.counter % 100 == 0:
                self.menu.action = OverlayMenu.ACTION_CLOSE
            
            self.text_pub.publish(self.overlaytext)
            # If values are very high it autoadjusts so be careful
            self.value_pub.publish(math.cos(self.counter * math.pi * 2 / 1000))
            self.menu_publisher.publish(self.menu)
            
            self.rate.sleep()
            self.counter += 1
    
    def start_harodistance_demo(self):
        
        while not rospy.is_shutdown():
            self.overlaytext = self.update_overlaytext(number=self.plot_value, number2=self.plot_value_y, number3=self.piechart_value)
            self.menu = self.update_overlay_menu_haro_tf()
            
            self.text_pub.publish(self.overlaytext)
            
            self.plot_value_pub.publish(self.plot_value)
            self.plot_value_pub_y.publish(self.plot_value_y)
            self.piechart_value_pub.publish(self.piechart_value)
            
            self.menu_publisher.publish(self.menu)
            
            self.rate.sleep()
            self.counter += 1
  


  
def dummy_overlay_demo():
    rospy.init_node('drone_Pose', anonymous=True)
    haro_overlay_object = Droneheight()
    try:
        #haro_overlay_object.start_dummy_demo()
        haro_overlay_object.start_harodistance_demo()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    dummy_overlay_demo()


