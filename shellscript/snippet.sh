#!bash

#use under normal linux environment
#!/bin/bash 

#----------------------
for i in {a..c}; do echo $(printf "%s %d" "$i" "''$i"); done

#----------------------
VAR=abcdef
echo ${VAR:${#VAR}-3:${#VAR}-1}

#----------------------
A=1
B=2
echo $((A+B))

#----------------------
RANDOM=`date +%s`
echo $RANDOM
echo $RANDOM

#----------------------
function_test()
{
    echo "0:"$0
    echo "1:"$1
    echo "2:"$2
    echo "@:"$@
    echo "#:"$#
}

function_test arg1 arg2
#---------------------- [network check port]
#[CLS]: check with "netstat -tulpn | grep LISTEN"
#[CLS]: check with "lsof -i -P -n | grep LISTEN"
(echo > /dev/tcp/localhost/20) > /dev/null 2>&1
result=$?
echo "resutl=$result"
if [ $result -eq 0 ]; then
    echo "20 port open"
else
    echo "20 port closed"
fi

#---------------------- [network scan port]
for (( port=630; port<=635; port++ ))
    do
        (echo > /dev/tcp/127.0.0.1/$port) > /dev/null 2>&1
        result=$?
        echo "resutl=$result"
        if [ $result -eq 0 ]; then
            echo "$port open"
        else
            echo "$port closed"
        fi
    done