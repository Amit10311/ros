cmake_minimum_required(VERSION 3.0.2)
project(classes)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  my_custom_srv_msg_pkg
)


###################################
## catkin specific configuration ##
###################################

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES classes
#  CATKIN_DEPENDS roscpp std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(bb8_move_circle_class src/bb8_move_circle_class.cpp)

add_dependencies(bb8_move_circle_class
 ${bb8_move_circle_class_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(bb8_move_circle_class
   ${catkin_LIBRARIES}
 )

 add_executable(bb8_move_stop_circle_class src/bb8_move_stop_circle_class.cpp)

add_dependencies(bb8_move_stop_circle_class
 ${bb8_move_circle_class_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(bb8_move_stop_circle_class
   ${catkin_LIBRARIES}
 )

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_classes.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
