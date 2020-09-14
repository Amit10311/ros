# Subscribe data

```bash
void counterCallback(const sensor_msgs::PointCloud2::ConstPtr& msg)        // Define a function called 'callback' that receives a 
{
  ROS_INFO("%s", msg->header.frame_id.c_str());          //  Header header

  //ROS_INFO("%f", msg->twist.twist.linear.x);
  //ROS_INFO("%f", msg->pose.pose.position.x);

  ROS_INFO("%d", msg->width);      //        uint32 height

  ROS_INFO("%d", msg->height);   //   uint32 width 
 //  ROS_INFO("%s", msg->is_dense.bool; 
```
[ PCL tutorial in ROS](http://library.isr.ist.utl.pt/docs/roswiki/perception_pcl(2f)Tutorials.html)


[PCL Overview](http://wiki.ros.org/pcl/Overview)


[ros msg](http://wiki.ros.org/msg)

