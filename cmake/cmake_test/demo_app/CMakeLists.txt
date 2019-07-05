cmake_minimum_required (VERSION 3.5)

#include(../sdk_rtos/CMakeLists.txt)
add_subdirectory(../sdk_rtos/ ${CMAKE_CURRENT_BINARY_DIR}/sdk)

project (demo_app)

link_libraries(rtos)
add_executable(demo_app main_app.c)
