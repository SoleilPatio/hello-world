/*
 ============================================================================
 Name        : preprocessor_test.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

/*
 *[CLS]: 1.1: # is all about string. It's a Unary Operation
 *	 1.2: # is to transform a token into string, not concatnate two strings
 */
#define JOINSTR1(a,b)  a # b
#define JOINSTR2(a,b)  a  b
#define JOINSTR3(a,b)  #a #b

/*
 * [CLS]: 2.1: ## is all about variable name or symbol name
 * 	  2.2: ## is to concatenate 2 token into a "new token" (variable)
 */
char *book_string = "This is a book";
#define JOINSTR4(a,b)  a ## b


int main(void) {
	puts("Hello World!!!"); /* prints Hello World!!! */

	printf("%s\n", JOINSTR1("This is ","a book")); /*[CLS]: output==>This is "a book"*/
	printf("%s\n", JOINSTR1("This is ",a book)); /*[CLS]: output==>This is a book*/
	printf("%s\n", JOINSTR2("This is ","a book")); /*[CLS]: output==>This is a book*/
	printf("%s\n", JOINSTR3("This is ","a book")); /*[CLS]: output==>"This is ""a book"*/
	printf("%s\n", JOINSTR4(book,_string)); /*[CLS]: output==>This is a book*/


	return EXIT_SUCCESS;
}
