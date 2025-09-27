#!/bin/bash

no=4

for i in 1 2 3 4 5 6 7 8 
do
    if [[ $no -eq $i ]]
    then 
    echo "No is found $i"
    break
    fi
    echo "number is $i"
done