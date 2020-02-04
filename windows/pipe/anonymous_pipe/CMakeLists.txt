cmake_minimum_required (VERSION 2.6)

set(CMAKE_SYSTEM_NAME Generic)      #[CLS] cross compiler
project (anonymous_pipe C CXX ASM)  #[CLS] "C CXX ASM" skip gcc test under cross compiler


#[CLS]: tell all target to link these libraries ==> equal  -lws2_32 
# link_libraries(ws2_32 wsock32)

add_executable(a.exe a.cpp)
add_executable(b.exe b.cpp)
