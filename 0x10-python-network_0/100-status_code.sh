#!/bin/bash
# only status code
curl -s -i -L "$1" | grep -E "HTTP/" | cut -d ' ' -f 2
