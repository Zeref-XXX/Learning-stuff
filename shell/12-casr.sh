#!/bin/bash
 
 echo   "choose  a for date 
        b for ls
        c for pwd
        "
 read choice

 case $choice in
    a) date;;
    b) ls;;
    c) pwd;;
    *) echo "INvalid input"
esac