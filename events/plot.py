# Standard imports
import numpy as np
import matplotlib.pyplot as plt
import base64
import io

np.random.seed(10)

# Create a random image
image = np.random.randn(100, 100)

# Place the png as a binary in memory
plt.imshow(image)
buffer = io.BytesIO()
plt.savefig(buffer, format="png") 

# Create the data
data = buffer.getvalue()      # Get the data from the buffer
data = base64.b64encode(data) # Encode to base64 bytes
data = data.decode()          # Convert bytes to string
print('Data:', type(data), data[:25])

# Write the data to a webpage
file = "test.html"
with open(file, 'w') as f:
    print("Writing to file:", file)
    f.write(f"<html><body><img src='data:image/png;base64,{data}'></body></html>")