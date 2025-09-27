#!/bin/bash


# id=$UID
# if [[ id -eq 0 ]]

if [[ $UID -eq 0 ]]
    then
    echo "Root user"
else
    echo "NOT Root user"
fi
  