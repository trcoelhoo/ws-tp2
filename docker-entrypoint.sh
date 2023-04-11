#!/bin/sh
# bash file with your commands

PORT=7201
URL='http://localhost:'$PORT'/rest/repositories'
URL2=$URL'/books/import/server'
echo $URL
echo $URL2

curl -X POST $URL -H 'Content-Type: multipart/form-data' -F 'config=@repo-config.ttl'

#curl -X POST --header 'Content-Type: application/json' \
#-d '{
#  "fileNames": [
#    "@./books.nt"
#  ]
#}' $URL2