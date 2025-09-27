#!/bin/bash

count=0
num=100

while [[ $count -le $num ]]
do 
    echo "number is $count "
    let   count++
done