#!/bin/bash

# Check if the file path argument is provided
if [ $# -eq 0 ]; then
  echo "Please provide a file path as an argument"
  exit 1
fi

# Check if the file exists
if [ ! -f $1 ]; then
  echo "File not found"
  exit 1
fi

# Upload the file to keep.sh and get the link
link=$(curl --upload-file $1 https://free.keep.sh 2>/dev/null)

# Check if the upload was successful
if [ $? -ne 0 ]; then
  echo "Upload failed"
  exit 1
fi

# Print the link
echo "Link: $link"

