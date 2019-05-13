#!/bin/bash

author="strindberg"

for i in authors/$author/plays/* ; do
    if [ -d $i ]; then
	echo directory
    else
	echo $i
	stem=$(echo $i | cut -d"." -f 1)
	echo $stem
	mkdir $stem
	cp $i $stem/play.txt
    fi
done
