/*
 ============================================================================
 Name        : lldb-python-script.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int foo_2(int b, int c) {
	char buffer[] = "This is 2!\n";

	printf(buffer);

	return 2;
}


int foo_1(int a) {
	int ret;
	int count = 0;
	char buffer[255] = "I am foo_1\n";

	printf(buffer);

	while( count <= 1000) {
		count += 1;
		printf("count = %d\n", count);
		ret = foo_2(456, 789);

	}



	return ret;

}



int main(void) {
	puts("!!!Hello World!!!"); /* prints !!!Hello World!!! */
	foo_1(123);


	return EXIT_SUCCESS;
}


