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

#Enable testing for current directory and below.
enable_testing() #[CLS] 或者用option(BUILD_TESTING "" OFF)

include(Dart)                       #[CLS] 產生 DartConfiguration.tcl (cmake configure的時候產生)
#link_libraries(rtos)

add_executable(test1 ${CMAKE_CURRENT_SOURCE_DIR}/test1.c)
add_test(NAME test1 COMMAND test1)  #[CLS] 這種寫法會造成CTestTestfile.cmake 裏面的命令帶路徑並加上.exe

add_executable(test2 ${CMAKE_CURRENT_SOURCE_DIR}/test2.c)
add_test( test2  test2)             #[CLS] 這種寫法會造成CTestTestfile.cmake 裏面的命令沒有帶路徑(反而容易跨平臺)
# add_test(NAME test2 COMMAND test2)


#Add sub directory
add_subdirectory(sub_src)

#[CLS] print "ctest" command
message("CMAKE_CTEST_COMMAND=" ${CMAKE_CTEST_COMMAND})
