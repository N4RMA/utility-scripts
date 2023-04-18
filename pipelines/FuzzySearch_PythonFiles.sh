#!/bin/bash
# FuzzySearch_PythonFiles.sh
#
# This script performs an interactive fuzzy search on the content of all
# Python files (*.py) in the current directory and its subdirectories.
# It uses grep for searching and fzf for interactive filtering.
# The search is case-insensitive and displays line numbers with the results.
# Colored output is preserved in the fzf interface.
#
# Usage: Run the script in the directory where you want to search.
#
grep -r --color=always --include='*.py' -n -i '' * | fzf --ansi
