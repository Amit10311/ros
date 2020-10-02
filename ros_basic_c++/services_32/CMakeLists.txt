cmake_minimum_required(VERSION 3.0.2)
project(services_32)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  roslib
  iri_wam_reproduce_trajectory
)



###################################
## catkin specific configuration ##
###################################

catkin_package(
  INCLUDE_DIRS include
 #  LIBRARIES services_32
  CATKIN_DEPENDS iri_wam_reproduce_trajectory roscpp roslib
#  DEPENDS system_lib
)

###########
## Build ##
###########

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


add_executable(file_execute_trajectory src/file_execute_trajectory.cpp)

add_dependencies(file_execute_trajectory 
      ${file_execute_trajectory_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(file_execute_trajectory 
   ${catkin_LIBRARIES}
 )

