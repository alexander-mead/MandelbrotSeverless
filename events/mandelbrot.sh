#!/bin/zsh

curl -i -X POST http://127.0.0.1:3000/mandelbrot \
    -H 'Content-Type: application/json' \
    --data-binary @- << EOF
{
    "x": 2.,
    "y": 1.,
}
EOF