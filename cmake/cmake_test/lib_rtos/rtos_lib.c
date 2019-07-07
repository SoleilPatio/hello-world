#include <stdio.h>
#include "rtos_lib.h"
#include "rtos_lib_public.h"

int rtos_func(int argc) {

	printf("I am Demo rtos_func: %d!\n", argc);
	return 0;
}

int rtos_func_public(int argc) {
	printf("Public RTOS function!%d\n", argc);
		return 0;
}
