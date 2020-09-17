1. http://www.cplusplus.com/reference/cstdio/printf/
```bash
%d is for int
%c is for char
%f is for float
("%s", msg->header.frame_id.c_str());                 Header header
```

2 http://wiki.ros.org/roscpp/Overview/Parameter%20Server
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
3. http://docs.ros.org/diamondback/api/rostime/html/classros_1_1Rate.html
```bash
#include <rate.h>

ros::Rate loop_rate(2);     // object of 2Hz
// 2 cycles/s
```
4. http://docs.ros.org/indigo/api/roscpp/html/classros_1_1Publisher.html
```bash
#include <publisher.h>
```
