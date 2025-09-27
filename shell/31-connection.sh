#!/bin/bash

read -p "Enter the site " site

ping $site

if [[ $? -eq 0 ]]
    then
    echo "successs"
else
echo "failed"
fi