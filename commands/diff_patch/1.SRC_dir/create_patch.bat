REM -a 將所有檔案都視為文字檔
REM -u 輸出預設三行的相同文字行
REM -r 遞迴比較所有的子目錄
REM -N 將缺少的檔案視為空檔案

REM from "tool_dir_ORG" to "tool_dir"
diff -Naur tool_dir_ORG tool_dir | tee diff.patch