#!/bin/bash

if [ $1 ]
    then
    case $1 in 
        up)
            docker-compose -f docker-compose.yml up
            ;;
    esac
else
    echo 'No argument given!'
fi