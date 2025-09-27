#!/bin/bash

myvar="HELLOlllo TiTis is a sample variable"

var2=${#myvar}

echo "original --- ${myvar}"
echo "copied in var2 $var2"

echo "uppercase myvar is ${myvar^^}"
echo "lowercase myvar is ${myvar,,}"

cha=${myvar/sample/changesd}
echo "changes in original  ${cha}"

slice=${myvar:2:5}
echo "sliced $slice"