# Standard imports
import requests
import sys

# Parameters
#URL = "http://127.0.0.1:3000"
URL = "https://0hku56rtzd.execute-api.eu-west-1.amazonaws.com/Prod"
OUT = "mandelbrot.html"

# Welcome
print()
print('Attemping to generate Mandelbrot data')

# This is the data that will be sent to the server
headers = {"Content-Type": "application/json"}
data = {}
data["real"] = sys.argv[1] if len(sys.argv) > 1 else -0.5
data["imag"] = sys.argv[2] if len(sys.argv) > 2 else 0.
data["size"] = sys.argv[3] if len(sys.argv) > 3 else 2.
print('Data being sent:', data)
print()

# Make the request
r = requests.post(URL+"/mandelbrot", headers=headers, json=data)

# This is the data returned from the server
print("Return from request:", type(r), r)
print("Return from request:", type(r.json()), r.json().keys())#, r.json())
print("Return from request:", type(r.json()["data"]))#, r.json()["data"])

# Convert the data format
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

# TODO: Print the data using matplotlib, rather than make a webpage
# Write the data to a webpage
with open(OUT, "w") as f:
    print("Writing to file:", f.name)
    f.write(f"<html><body><img src='data:image/png;base64,{data}'></body></html>")
print("Done\n")