#!/bin/bash

# while IFS="," read id name age
cat test.csv  | awk 'NR!=1 {print}' |
while  IFS=',' read id name age
do
    echo "$id"
done < test.csv