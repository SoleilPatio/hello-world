cmake_minimum_required (VERSION 3.5)

#[CLS]: assign toolchain
#       BETTER place before project() for unknown reason
set(CMAKE_C_COMPILER x86_64-w64-mingw32-gcc CACHE FILEPATH "cross compiler" FORCE)
set(CMAKE_CXX_COMPILER x86_64-w64-mingw32-c++ CACHE FILEPATH "cross compiler" FORCE)


project (google_test_sample)


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

#[CLS]: add google test cmake directory (out-of-source need binary directory)
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../googletest ${CMAKE_CURRENT_BINARY_DIR}/googletest)

#[CLS]: enable cmake testing for current directory and below
enable_testing()

add_executable(main ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp)
target_link_libraries(main gtest_main)  #[CLS]: 如果有link gtest_main, 在這行會自動include gtest_main的include path
add_test(NAME main-test1 COMMAND main)
add_test(main-test2 main)

#[CLS]: include directory
# include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

#[CLS]: compiler option
# add_compile_options(-std=c++11)

#[CLS]: link option
# add_link_options(-static)
# target_link_options(main_app -static)
# target_link_libraries(main_app -static)
