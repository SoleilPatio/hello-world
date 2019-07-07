macro(SHOW_VAR var_name)
	message( "[info] ${var_name}=${${var_name}}")
endmacro(SHOW_VAR)


#######################################################################
#[CMAKE_INSTALL_PREFIX]
#Win   C:/Program Files (x86)/sdk_rtos
#UINIX /usr/local
#######################################################################
SHOW_VAR(CMAKE_INSTALL_PREFIX) 


#######################################################################
#[DESTDIR]
#		$make DESTDIR=/home/john install
#		will install to $DESTDIR/$CMAKE_INSTALL_PREFIX/....
#######################################################################
SHOW_VAR(DESTDIR)

#path of current file
SHOW_VAR(CMAKE_CURRENT_LIST_FILE)



SHOW_VAR(_IMPORT_PREFIX)
SHOW_VAR(CMAKE_CURRENT_SOURCE_DIR)
SHOW_VAR(CMAKE_CURRENT_BINARY_DIR)
SHOW_VAR(CMAKE_INSTALL_LIBDIR)