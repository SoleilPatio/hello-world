
REM 重複patch 可以revert
REM patch.exe -p0 -i diff.patch

REM 純測試
patch.exe --dry-run --verbose p0 -i diff.patch
