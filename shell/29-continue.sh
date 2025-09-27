#!/bin/bash

for i in 1 2 3 4 5 6 7 8 
do
    let rem=$i%2
    if [[ $rem -eq 0 ]]
    then
            continue
    fi
    echo "number is $i"
done