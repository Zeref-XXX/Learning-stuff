#!/bin/bash

if [[ $# -eq 0 ]]
    then
    echo "No argument given "
    exit 
fi

for file in $@
do
echo "files are $file"

done