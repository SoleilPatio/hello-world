cmake_minimum_required (VERSION 2.6)

set(CMAKE_SYSTEM_NAME Generic)      #[CLS] cross compiler (-remove rdynamic)

project (anonymous_pipe)


#[CLS]: tell all target to link these libraries ==> equal  -lws2_32 
# link_libraries(ws2_32 wsock32)

add_executable(main.exe main.cpp)
add_executable(child.exe child.cpp)

