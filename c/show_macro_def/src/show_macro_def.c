/*
 ============================================================================
 Name        : show_macro_def.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

/*[CLS]:a complex flag that we want to know*/
#define A_COMPLEX_FLAG	((A+B)+C-D)*E*F


/*[CLS]:step1: level 1 macro to expand as a string*/
#define L1_TOSTR(def) #def

/*[CLS]:output of below line is:  #pragma message: Only L1=A_COMPLEX_FLAG
 * ==>  no expansion of A_COMPLEX_FLAG, because "it is on the left, only macro on the left be expanded"
 * */
#pragma message ("Only L1="L1_TOSTR(A_COMPLEX_FLAG))

/*[CLS]:step2: level 2 only put level-1 on the right to force macro expansion happend*/
#define L2_TOSTR(def) L1_TOSTR(def)

/*[CLS]:output of below line is: #pragma message: Add L2=((A+B)+C-D)*E*F
 *  ==> Good!
 * */
#pragma message ("Add L2="L2_TOSTR(A_COMPLEX_FLAG))



int main(void) {
	puts("Hello World!!!"); /* prints Hello World!!! */
	return EXIT_SUCCESS;
}
