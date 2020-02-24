cmake_minimum_required (VERSION 3.5)

project (main_app)


#[CLS][Case1]:	source build
#		"source build" must before "lib build",or "redefine target" will happen
#add_subdirectory(../lib_rtos/ ${CMAKE_CURRENT_BINARY_DIR}/lib_rtos)

###include_directories(../lib_rtos/include) #no need to set include path.

#[CLS][Case2]: lib build
#	   export.cmake just like "c include header", check #ifdef at the beginning, 
#	   so no need to worry about redefine target
#	   install() command will generate code to calculate _IMPORT_PREFIX	
#set(SDK_HOME	${CMAKE_CURRENT_SOURCE_DIR}/../SDK_HOME)
#include ("${SDK_HOME}/cmake/librtos.cmake")

###include_directories(${SDK_HOME}/include) #no need to set include path.



#link_libraries(rtos)
add_executable(test3 ${CMAKE_CURRENT_SOURCE_DIR}/test3.c)
add_test(NAME test3 COMMAND test3)
