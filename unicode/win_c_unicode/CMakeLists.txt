cmake_minimum_required (VERSION 2.6)

set(CMAKE_SYSTEM_NAME Generic)      #[CLS] cross compiler (-remove rdynamic)

project (win_c_unicode)


#[CLS]: tell all target to link these libraries ==> equal  -lws2_32 
# link_libraries(ws2_32 wsock32)


add_executable(print_test.exe print_test.cpp)
add_executable(fopen_test.exe fopen_test.cpp)

add_executable(main.exe main.cpp)
add_executable(wmain.exe wmain.cpp)
target_link_options(wmain.exe PUBLIC -municode) #[CLS]: -municode  : for mingw unicode support


