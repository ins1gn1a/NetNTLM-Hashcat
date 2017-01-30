#!/bin/bash

# Dirty script

cat $1 | sed -e 's/ \+/:/g' | awk -F':' '{tmp=$4;$4=$3;$3=tmp;print}' | sed -e 's/ \+/:/g' | sed "s/:/::/" | sed 's/:$//'
