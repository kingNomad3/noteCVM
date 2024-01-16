#!/bin/bash

faireEspace(){

for((i=0;i<$1;i++))
do  
    echo  -n " "
done   
}


for ((i=0;i<10;i++))
do
        clear 
        faireEspace $i

        if [[ $i -lt 9 ]]
        then
            echo "@"
        else
            echo "BOOM"
        fi

        sleep 0.1
done