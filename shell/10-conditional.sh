#!/bin/bash

read -p "ENter the marks : " marks

if [[ $marks -gt 40 ]]
    then
        echo "marks is greater than 40"
else    
    echo "marks is less than 40"
fi