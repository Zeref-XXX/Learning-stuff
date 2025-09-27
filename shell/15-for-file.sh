#!/bin/bash

path=$(pwd)


echo "addded in the file.txt " >> "$path/file.txt"

item="$path/file.txt"

for item in $(cat $item)
do
    echo "$item"
done