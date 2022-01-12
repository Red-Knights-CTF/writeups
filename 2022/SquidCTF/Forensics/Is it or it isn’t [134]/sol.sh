#!/bin/bash
stegsnow -p frontman -C status.txt | awk '$0="SCTF{"$0"}"' 
