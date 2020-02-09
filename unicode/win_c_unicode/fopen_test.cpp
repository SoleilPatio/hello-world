#include <stdio.h>
#include <locale.h>

void WStrTest(wchar_t *wstr, int count)
{
    int i;

    printf("[Printf]:\n");
    printf("%ls\n", wstr);
    printf("[End of printf]\n");

    printf("[Raw]:");
    for (i = 0; i < count; i++)
        printf("%04x ", wstr[i]);
    printf("\n");

    FILE *file;
    file = _wfopen(wstr, L"w");
    if( file )
        printf("Open file Success:%x\n",file);
    else
        printf("Open file Failed:%x\n",file);

}

void StrTest(char *str, int count)
{
    int i;

    printf("[Printf]:\n");
    printf("%s\n", str);
    printf("[End of printf]\n");

    printf("[Raw]:");
    for (i = 0; i < count; i++)
        printf("%02x ", (unsigned char)str[i]);
    printf("\n");

    
    FILE *file;
    file = fopen(str, "w");
    if( file )
        printf("Open file Success:%x\n",file);
    else
        printf("Open file Failed:%x\n",file);

}

/*[CLS]:
    Windows 開檔案:
        1.只要注意不要把utf-8 encoded string,傳進去api裏面就好
        2.big-5給進去貌似核心會處理，成功
        3.wchar unicode傳給_wfopen版本，成功
    Linux 是UTF-8核心，linux command shell傳進來的是utf-8編碼
*/

int main(int argc, char *argv[], char *envp[])
{
    int i;

    printf("#1: ---------------------------------------------------------------------------------------\n");
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL)); //[CLS]: original locale is C , 這樣印不出來
    wchar_t ws1[] = L"正能量";                          //[CLS]: source code編碼是utf-8 , 用L""儲存後，ws1[]裏面是UCS-2 unicode i.e: [ 正 ] [ 能 ] [ 量 ] ==>[ u'\u6b63' ] [ u'\u80fd' ] [ u'\u91cf' ]
    WStrTest(ws1, sizeof(ws1) / sizeof(wchar_t));

    printf("#2: ---------------------------------------------------------------------------------------\n");
    setlocale(LC_ALL, "");                              //[CLS]: change locale to environment selected : Chinese (Traditional)_Taiwan.950
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
    wchar_t ws2[] = L"正能量";
    WStrTest(ws2, sizeof(ws2) / sizeof(wchar_t));

    printf("#3: ---------------------------------------------------------------------------------------\n");
    setlocale(LC_ALL, "C"); //[CLS]: change locale to "C"
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
    wchar_t ws3[] = {0x6b63, 0x80fd, 0x91cf, 0x0000}; //[CLS]: 手動寫進unicode , 正能量
    WStrTest(ws3, sizeof(ws3) / sizeof(wchar_t));

    printf("#4: ---------------------------------------------------------------------------------------\n");
    setlocale(LC_ALL, ""); //[CLS]: change locale to "C"
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
    wchar_t ws4[] = {0x6b63, 0x80fd, 0x91cf, 0x0000}; 
    WStrTest(ws4, sizeof(ws4) / sizeof(wchar_t));


    printf("#5: ---------------------------------------------------------------------------------------\n");
    setlocale(LC_ALL, "C"); 
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
    char str1[] = "正能量"; 
    StrTest(str1, sizeof(str1) / sizeof(char));

    printf("#6: ---------------------------------------------------------------------------------------\n");
    setlocale(LC_ALL, "");
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
    char str2[] = "正能量"; 
    StrTest(str2, sizeof(str2) / sizeof(char));


    printf("#7 (Anscii Character): ---------------------------------------------------------------------------------------\n");
    setlocale(LC_ALL, "C"); 
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
    char str3[] = "abc123"; 
    StrTest(str3, sizeof(str2) / sizeof(char));

    if( argc > 1 )
    {
        printf("#8 (argc[1]) ): ---------------------------------------------------------------------------------------\n");
        setlocale(LC_ALL, "C"); 
        printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
        StrTest(argv[1], sizeof(argv[1]) / sizeof(char));

        printf("#9 (argc[1]) ): ---------------------------------------------------------------------------------------\n");
        setlocale(LC_ALL, ""); 
        printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
        StrTest(argv[1], sizeof(argv[1]) / sizeof(char));
    }





    return 0;
}