#!/bin/bash
# cURL only methods
curl -X OPTIONS "$1" -si | grep Allow | cut -d' ' -f 2-
