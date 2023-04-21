#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Please provide a filename as an argument."
  exit 1
fi

filename=$1

if [ ! -f $filename ]; then
  echo "File not found."
  exit 1
fi

output=$(curl -s bashupload.com -T $filename)

echo "$output" | awk '/wget/ {print}'

