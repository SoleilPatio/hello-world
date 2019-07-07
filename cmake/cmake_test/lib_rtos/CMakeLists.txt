cmake_minimum_required (VERSION 3.5)
include(../cmake/util.cmake)

project (sdk_rtos)

#######################################################################
#Define target:
#		1. library
#		2. public header files
#		3. use ";" to add multiple files
#######################################################################
add_library(rtos rtos_lib.c)
set_target_properties(rtos PROPERTIES PUBLIC_HEADER 
							"./include/rtos_lib.h;./public_include/rtos_lib_public.h"
							)

include_directories(./include)
include_directories(./public_include)


#######################################################################
#[CLS]: seems the below do not have any benefits
#INSTALL_INTERFACE : seems has no effect at any aspects
#BUILD_INTERFACE : will add to -Ixxxx in this build, but no effect to export
#######################################################################
#include_directories($<INSTALL_INTERFACE:public_include_install_1> 
#					$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/public_include>)


#target_include_directories(rtos PUBLIC 
#							$<INSTALL_INTERFACE:public_include> 
#							$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/public_include>
#							)


#######################################################################
#Use CMAKE_INSTALL_PREFIX to assign install path,
# (instead of DESTINATION variable)
#######################################################################
set(SDK_HOME ${CMAKE_CURRENT_SOURCE_DIR}/../SDK_HOME)
#set (CMAKE_INSTALL_PREFIX "${SDK_HOME})
if (CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
    set (CMAKE_INSTALL_PREFIX "${SDK_HOME}" CACHE PATH "default install path" FORCE )
endif()

SHOW_VAR(SDK_HOME)
SHOW_VAR(CMAKE_INSTALL_PREFIX)

#######################################################################
# if DESTINATION has full path value ==> export absolute install
# if DESTINATION has relative path   ==> install relative to CMAKE_INSTALL_PREFIX
#										 which means you can move directory to any where
#
#
# INCLUDES DESTINATION :
#					0. INCLUDES is path, while PUBLIC_HEADER are headers
#					1. copy no files. use "PUBLIC_HEADER" property to copy
#					2. add path to INTERFACE_INCLUDE_DIRECTORIES of which that import it
#
#######################################################################
#Absolute path install (because CMAKE_BINARY_DIR=C:/.... or /usr/home/...)
#install(TARGETS rtos	DESTINATION ${CMAKE_BINARY_DIR}/installed/lib EXPORT librtos LIBRARY )
#install(EXPORT librtos	DESTINATION ${CMAKE_BINARY_DIR}/installed/cmake)

#Relative install to CMAKE_INSTALL_PREFIX
install(TARGETS rtos
		EXPORT librtos
		LIBRARY 		DESTINATION lib
		INCLUDES 		DESTINATION include
		PUBLIC_HEADER	DESTINATION include
		 )

install(EXPORT librtos	
		DESTINATION cmake)

install(FILES link_script_1.ld link_script_2.ld
        DESTINATION lib/link_script
)










