#!/bin/zsh

# Curl command to trigger the Mandelbrot lambda function
curl -i -X POST http://127.0.0.1:3000/mandelbrot \
    -H 'Content-Type: application/json' \
    --data-binary @- << EOF
{ 
    "real": "-0.5", 
    "imag": "0.", 
    "size": "2." 
}
EOF