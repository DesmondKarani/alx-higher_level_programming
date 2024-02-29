#!/bin/bash
# This script takes a URL as an argument and displays the size of the response body in bytes
[ $# -eq 0 ] && echo "Usage: $0 URL" && exit 1 || echo $(curl -s -w "%{size_download}" -o /dev/null "$1")

