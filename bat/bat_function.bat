@echo off
@echo [bat start]

@echo [call function]
@call :FOO
@echo [return from function]

@echo [call function]
@call :BAR 123 "I am C"
@echo [return from function]


@echo [if loop start]
if "" == "" (
		REM [CLS] !time! must use with enable delayed expansion option 
		@setlocal enabledelayedexpansion
		@echo time is !time!
	)
@echo [if loop end]	
	
	
@echo [bat end]

REM [CLS] /B means exit from batch not command shell
@exit /B 0



:FOO
	@echo [	FOO enter]
	@echo [	FOO leave]
	@exit /B 0
	
:BAR
	@echo [	BAR enter]
	echo "	%%~0:" %~0
	echo "	%%~1:" %~1
	echo "	%%~2:" %~2
	echo "	%%~3:" %~3
	echo "	%%0:" %0
	echo "	%%1:" %1
	echo "	%%2:" %2
	echo "	%%3:" %3

	
	@echo [	BAR leave]
	@exit /B 0




