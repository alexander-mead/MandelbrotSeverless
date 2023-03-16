#import numpy as np
import requests
#import matplotlib.pyplot as plt
#from PIL import Image
#import io
#import base64

# This is the data that will be sent to the server
headers = {"Content-Type": "application/json"}
data = { 
    "real": "-0.5", 
    "imag": "0.", 
    "size": "2." ,
}
r = requests.post("http://127.0.0.1:3000/mandelbrot", headers=headers, json=data)

# This is the data returned from the server
print('Return from request:', type(r), r)
print('Return from request:', type(r.json()), r.json().keys())#, r.json())
print('Return from request:', type(r.json()["data"]))#, r.json()["data"])

# Convert the data
data = r.json()["data"]
print("First 25 characters of data:", data[:25])
#data = bytes(data, "utf-8")
#data = data.decode("base64")

#image = Image.open(io.BytesIO(data))

# incoming_data = r.json()["data"] # This comes in as a string
# converted_data = bytes(incoming_data, "utf-8")
# #io.BytesIO()
# #png.decode("base64")
# image = Image.open(io.BytesIO(converted_data))
# image.show()

# Write the data to a webpage
file = "test.html"
with open(file, "w") as f:
    print("Writing to file:", file)
    f.write(f"<html><body><img src='data:image/png;base64,{data}'></body></html>")