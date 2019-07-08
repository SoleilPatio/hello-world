cmake_minimum_required (VERSION 3.5)
include(../cmake/util.cmake)

project (sdk_rtos)

#######################################################################
#Define target:
#		1. library
#######################################################################
add_library(rtos rtos_lib.c)

#######################################################################
#[includes handling]:
#		1. public header files
#			1-1. use ";" to add multiple files
#			1-2. PUBLIC_HEADER property can be used in install copy phase 
#		2. ONLY target_*** version of include command can set PUBLIC
#			2-1. BUILD_INTERFACE :   will add to include path who add_subdirectory it
#			2-2. INSTALL_INTERFACE : will add to include path who import this
#			
#######################################################################
#1.
set_target_properties(rtos PROPERTIES PUBLIC_HEADER 
							"./include/rtos_lib.h;./public_include/rtos_lib_public.h"
							)


#2.
#use target_include_directories(), for target_version has PUBLIC to propagate
#include_directories(./include)
target_include_directories(rtos PUBLIC 
							$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
							$<INSTALL_INTERFACE:include>
							)
							
target_include_directories(rtos PUBLIC 
							$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/public_include>
							$<INSTALL_INTERFACE:include> #add path to who import this = prefix+include
							)



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










