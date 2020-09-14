#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>


void counterCallback(const sensor_msgs::PointCloud2::ConstPtr& msg)        // Define a function called 'callback' that receives a 
{
  ROS_INFO("%s", msg->header.frame_id.c_str());                     // Print the value 'data' inside the 'msg' parameter
  //ROS_INFO("%f", msg->twist.twist.linear.x);
  //ROS_INFO("%f", msg->pose.pose.position.x);

  ROS_INFO("%d", msg->width);   

  ROS_INFO("%d", msg->height);   
 //  ROS_INFO("%s", msg->is_dense.bool;

}



int main(int argc, char** argv) {

    ros::init(argc, argv, "pcl_sub_node");    // topic name 
    ros::NodeHandle nh;                        // node 
    
    ros::Subscriber sub = nh.subscribe("octomap_point_cloud_centers", 1000, counterCallback);   // 
    
    ros::spin();
    
    return 0;
}
