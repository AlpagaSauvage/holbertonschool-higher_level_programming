#!/bin/bash
# body size
curl -sI "$1" | grep -i Content-Length | wc -c
