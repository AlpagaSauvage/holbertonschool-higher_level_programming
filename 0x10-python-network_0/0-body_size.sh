#!/bin/bash
# body size
curl -sI "$1" | awk '/Content-Length/{print $2}'
