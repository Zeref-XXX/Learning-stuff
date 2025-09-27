#!/bin/bash

read -p "ENter the marks : " marks

if [[ $marks -gt 80 ]]
    then
            echo "first division "
elif [[ $marks -gt 60 ]]  
    then
    echo " 2nd division "
    else
        echo "not 1st and 2nd "
fi