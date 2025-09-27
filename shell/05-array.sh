#!/bin/bash

myArr=(1 2 hello 1.234  changes "you are there" )

echo "${myArr[0]}"

echo "${myArr[*]}"
#addding in array

myArr+=(new things "adddede here")

echo "added some ;-  ${myArr[*]}"


#get length of array

echo "length of array ${#myArr[*]}"

echo "all values from 2nd are  ${myArr[*]:1} "

echo "specific value from 2 to 4 are ${myArr[*]:2:3}"
