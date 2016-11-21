cmake_minimum_required(VERSION 3.6)
project(stepikCourse)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

#set(SOURCE_FILES 7-Программирование_на_языке_Cpp/536/stepik-7_536-step14-1.cpp)
#set(SOURCE_FILES 7-Программирование_на_языке_Cpp/536/stepik-7_536-step14-2.cpp)
set(SOURCE_FILES 7-Программирование_на_языке_Cpp/536/stepik-7_536-step15.cpp)

add_executable(stepikCourse ${SOURCE_FILES})