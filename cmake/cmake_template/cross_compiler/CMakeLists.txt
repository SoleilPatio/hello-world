cmake_minimum_required (VERSION 3.5)


#[CLS]: avoid using -rdynamic
# set(CMAKE_SYSTEM_NAME "Generic" CACHE STRING "Target system." FORCE)

#[CLS]: assign toolchain
#       BETTER place before project() for unknown reason
set(CMAKE_C_COMPILER x86_64-w64-mingw32-gcc CACHE FILEPATH "cross compiler" FORCE)
set(CMAKE_CXX_COMPILER x86_64-w64-mingw32-c++ CACHE FILEPATH "cross compiler" FORCE)



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


#[CLS] set or unset
set(EXE_EXT ".exe")


#link_libraries(rtos)
add_executable(main_app${EXE_EXT} ${CMAKE_CURRENT_SOURCE_DIR}/main.c)
