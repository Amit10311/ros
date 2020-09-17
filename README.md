# ros
https://github.com/Amit10311/ros


# How to import directory
```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/AutonomyLab/ardrone_autonomy.git -b hydro-devel
$ cd ~/catkin_ws
$ catkin_make
```

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.


```bash
%d is for int
%c is for char
%f is for float
("%s", msg->header.frame_id.c_str());                 Header header
```
http://www.cplusplus.com/reference/cstdio/printf/



```bash
ros::Publisher _local_map_pub;

ros::NodeHandle n("~");
_local_map_pub = n.advertise<sensor_msgs::PointCloud2>("/map_generator/local_cloud", 1);
```
```bash
ros::NodeHandle nh("~");
std::string param;
nh.getParam("private_name", param);
```

http://wiki.ros.org/roscpp/Overview/Parameter%20Server

