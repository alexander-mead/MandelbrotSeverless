#!/bin/zsh

#baseURL="http://127.0.0.1:3000"
baseURL="https://0hku56rtzd.execute-api.eu-west-1.amazonaws.com/Prod"
URL=$baseURL"/mandelbrot"
output="mandelbrot.json"

echo ""
echo "URL: "$URL

# Curl command to trigger the Mandelbrot lambda function
curl -i -X POST $URL \
    -H 'Content-Type: application/json' \
    --output $output \
    --data-binary @- << EOF
{ 
    "real": "-0.5", 
    "imag": "0.", 
    "size": "2." 
}
EOF

# TODO: Create webpage to view data?