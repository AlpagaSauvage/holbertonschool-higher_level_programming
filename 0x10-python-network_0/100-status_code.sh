#!/bin/bash
# only status code
curl -o /dev/null -s -L -w '%{http_code}' "$1"
