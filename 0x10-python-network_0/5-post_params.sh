#!/bin/bash
# cURL POST parameters
curl -sv 'email=test@gmail.com' 'subject=I will always be here for PLD' -X POST "$1"
