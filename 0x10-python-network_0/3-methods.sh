#!/bin/bash
# body delete
curl -s -i -L "$1" -X OPTIONS | grep -E "Allow" | cut -d ' ' -f 2-
