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
}


int main(int argc, char *argv[], char *envp[])
{
    /* [CLS]:
        setlocale() 影響了printf輸出的行爲，輸入的資料都是widechar unicode raw data
        如果locale是default是C, 那應該會印出raw unicode,所以看不到東西
        如果locale是environment 950(Big-5), 那就能被console看到
        */

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
    setlocale(LC_ALL, "C"); //[CLS]: change locale to "C"
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
    char str1[] = "正能量"; 
    StrTest(str1, sizeof(str1) / sizeof(char));

    printf("#6: ---------------------------------------------------------------------------------------\n");
    setlocale(LC_ALL, ""); //[CLS]: change locale to "C"
    printf("Locale is: %s\n", setlocale(LC_ALL, NULL));
    char str2[] = "正能量"; 
    StrTest(str2, sizeof(str2) / sizeof(char));



    return 0;
}