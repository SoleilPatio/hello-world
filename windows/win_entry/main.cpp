#include <stdio.h>
#include <locale.h>

/*[CLS]: dos console 傳進來的是big-5 , short string不管怎麼樣的locale都可以印出去可以看到*/

void ShowArgs(int argc, char *argv[])
{
    int i;
    int j;
    for (i = 0; i < argc; i++)
    {
        printf("#%d: %s", i, argv[i]);
        printf("\n");
        printf("[raw]:");
        for (j = 0; argv[i][j] != 0; j++)
            printf("%02x ", (unsigned char)argv[i][j]);
        printf("\n");
    }
}

/* [CLS]: 
    1. main 傳進來的會是big-5 字串,不管怎麼樣的locale都可以印出去可以看到
    2. wmain 傳進來的就是widechar unicode了
    3. 傳進什麼跟console chcp (code page)無關?
*/

int main(int argc, char *argv[], char *envp[])
{
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL)); //[CLS]: original locale is C
    ShowArgs(argc, argv);

    setlocale(LC_ALL, ""); //[CLS]: change locale to environment selected : Chinese (Traditional)_Taiwan.950 (Big-5)
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
    ShowArgs(argc, argv);

    return 0;
}