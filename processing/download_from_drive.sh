#!/bin/bash
fileid="0B7XkCwpI5KDYNlNUTTlSS21pQmM"
filename="GoogleNews-vectors-negative300.bin.gz"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
