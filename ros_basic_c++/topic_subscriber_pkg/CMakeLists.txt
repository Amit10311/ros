cmake_minimum_required(VERSION 3.0.2)
project(topic_subscriber_pkg)
## Compile as C++11, supported in ROS Kinetic and newer
 add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)
## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

# catkin_python_setup()
################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES topic_subscriber_pkg
#  CATKIN_DEPENDS roscpp std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


# add_executable(${PROJECT_NAME}_node src/topic_subscriber_pkg_node.cpp)
# add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
# target_link_libraries(${PROJECT_NAME}_node
#   ${catkin_LIBRARIES}
# )

add_executable( simple_topic_subscriber src/simple_topic_subscriber.cpp)
add_dependencies( simple_topic_subscriber 
                 ${simple_topic_subscriber_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
                 
target_link_libraries(simple_topic_subscriber
   ${catkin_LIBRARIES}
 )
 
 
add_executable(odom_subscriber src/odom_subscriber.cpp)
add_dependencies(odom_subscriber 
                               ${odom_subscriber_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(odom_subscriber
   ${catkin_LIBRARIES}
 )
 


## either from message generation or dynamic reconfigure

## Specify libraries to link a library or executable target against

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
