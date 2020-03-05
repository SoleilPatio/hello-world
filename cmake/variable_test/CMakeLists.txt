#[CLS]: 加了這一行會正常
# cmake_minimum_required(VERSION 3.10) #[CLS]: 比較合邏輯
# cmake_minimum_required(VERSION 3.3)  #[CLS]: 舊的不合邏輯

if(1)
    message("==>if: (1) ---> OK!")
endif()


if(NOT 1)
    message("==>if: (NOT 1) ---> FALSE!")
else()
    message("==>else: if(NOT 1) ---> OK!")
endif()


#[CLS]: 測試option "ON" "OFF"的邏輯判斷
unset(option_on CACHE)
option(option_on "test option" ON ) #[CLS] 就算寫1, option_on 也是字串 "ON". option 是只能"ON"/"OFF"的字串變數
message("[INFO] option_on=${option_on}")


#[CLS]: CASE 1: 正確寫法. if()裏面會自動抓變數的值出來,因爲if()語法比${}還早設計
if(option_on) 
    message("==>if: (option_on) ---> OK!")
else()
    message("==>else: if(option_on) ---> FALSE!") 
endif()

if(NOT option_on)
    message("==>if: (NOT option_on) ---> FALSE!")
else()
    message("==>else: (NOT option_on) ---> OK!")
endif()

#[CLS]: CASE 2: 不對的寫法. 會變成if(NOT "ON") , 因爲 option_on 是一個 string "ON" , 拿來判斷NOT會出錯
if(NOT ${option_on}) 
    message("==>if: (NOT \${option_on}) ---> FALSE! NOTE: \"NOT\" \"ON\" is \"TRUE\"??")
else()
    message("==>else: (NOT \${option_on}) ---> OK! NOTE: \"NOT\" \"ON\" is \"TRUE\"??")
endif()

#[CLS]: 結論，不管是 option (string) 或是 數值 (-Dvar=1) , 在if()-else()判斷都用第一種寫法不要${}就好

set(var1 OFF)
set(var2 "var1")
if(${var2})
    message("==>if: (\${var2}) ---> FALSE!")
else()
    message("==>else: (\${var2}) ---> OK! [NOTE]: \${var2}->var1->OFF")
endif()

if(var2)
    message("==>if: (var2) ---> OK! [NOTE]: var2 is defined to a string which is TRUE")
else()
    message("==>else: (var2) ---> FALSE ")
endif()


if( "var2" )
    message("==>if: (\"var2\") ---> FALSE!  [NOTE]: all string are false if not > version 3.10")
else()
    message("==>else: (\"var2\") ---> OK! [NOTE]: all string except \"ON\" \"TRUE\" are all FALSE!")
endif()

