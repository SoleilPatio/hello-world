#include <stdio.h>
#include <locale.h>

void ShowArgs(int argc, wchar_t *argv[])
{
    int i;
    int j;
    for (i = 0; i < argc; i++)
    {
        printf("#%d: %ls", i, argv[i]);
        printf("\n");
        printf("[raw]:");
        for (j = 0; argv[i][j] != 0; j++)
            printf("%x ", argv[i][j]);
        printf("\n");
    }
}

/* [CLS]: 
    1. wmain 傳進來的會是unicode 字串(當然囉，如果是UTF-8誰來解碼?),不管console是不是big-5 code page
    2. 資料都對，就是wchar string印出去要正常，需要設定locale
*/

int wmain(int argc, wchar_t *argv[], wchar_t *envp[])
{
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL)); //[CLS]: original locale is C , widechar無法正常印出
    ShowArgs(argc, argv);

    setlocale(LC_ALL, ""); //[CLS]: change locale to environment selected : Chinese (Traditional)_Taiwan.950 (Big-5)
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
    ShowArgs(argc, argv);

    return 0;
}