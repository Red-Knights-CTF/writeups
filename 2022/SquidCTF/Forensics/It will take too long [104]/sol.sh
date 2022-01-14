#!/bin/bash
for ((i = 100; i > 0; i--)); do
    if [ ! -f "Zipped$i.zip" ]; then
        break
    fi
    unzip Zipped$i.zip
    rm Zipped$i.zip
done
clear
cat flag.txt
echo ""
