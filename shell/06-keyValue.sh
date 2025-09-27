#!/bin/bash

declare -A myArray

myArray=([name]=awesome [age]=3030)

echo "in myArray name is->  ${myArray[name]}"
