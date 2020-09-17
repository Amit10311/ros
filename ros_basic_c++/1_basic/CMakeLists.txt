cmake_minimum_required(VERSION 3.0.2)
project(my_package)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
)
## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

################################################
## Declare ROS messages, services and actions ##
################################################

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

## Generate dynamic reconfigure parameters in the 'cfg' folder
# generate_dynamic_reconfigure_options(
#   cfg/DynReconf1.cfg
#   cfg/DynReconf2.cfg
# )
###################################
## catkin specific configuration ##
###################################

## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES my_package
#  CATKIN_DEPENDS roscpp
#  DEPENDS system_lib
)

###########
## Build ##
###########


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
# add_library(${PROJECT_NAME}
#   src/${PROJECT_NAME}/my_package.cpp
# )

raries
## either from message generation or dynamic reconfigure
# add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

add_executable(simple src/simple.cpp)
add_executable(simple_loop src/simple_loop.cpp)

add_dependencies(simple simple_loop
      ${simple_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(simple 
   ${catkin_LIBRARIES}
 )

 target_link_libraries(simple_loop
   ${catkin_LIBRARIES}
 )

