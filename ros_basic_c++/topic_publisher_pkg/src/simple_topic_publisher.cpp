#include <ros/ros.h>
#include <std_msgs/Int32.h> // data type

int main(int argc, char **argv) {

  ros::init(argc, argv, "topic_publisher");
  ros::NodeHandle nh;

  ros::Publisher pub = nh.advertise<std_msgs::Int32>("counter", 1000); // 1 pub
  ros::Rate loop_rate(2);                                              // rate

  std_msgs::Int32 count; // create variable
  count.data = 0;        // initiate

  while (ros::ok()) {
    pub.publish(count); // assign the msg value to variable
    ros::spinOnce();    // call back
    loop_rate.sleep();  // maintain at rate
    ++count.data;       // increment the variable
  }

  return 0;
}