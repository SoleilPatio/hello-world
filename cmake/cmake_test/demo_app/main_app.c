#include <stdio.h>

extern int rtos_func(int argc);

int main(int argc, char **argv) {

	printf("I am Demo App!\n");

	rtos_func(999);
	return 0;
}
