cmake_minimum_required (VERSION 2.6)

project (winsock)


#[CLS]: tell all target to link these libraries ==> equal  -lws2_32 
link_libraries(ws2_32 wsock32)

add_executable(server server.cpp)
add_executable(client client.cpp)
