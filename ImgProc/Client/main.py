import socket
import cv2
import json
import base64
import numpy as np

# Read the image
img = cv2.imread("./0.jpg")

# Encode the image as a JPEG byte array
_, img_encoded = cv2.imencode('.jpg', img)

# Convert image data to base64 string
img_base64 = base64.b64encode(img_encoded)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port
host = socket.gethostname()
port = 9999

# Connect to the server
client_socket.connect((host, port))

# Prepare data to send
data = {
    'image': img_base64.decode('utf-8'),
    'message': 'Hello, server!'
}

# Serialize data to JSON
json_data = json.dumps(data)

# Send JSON data
client_socket.sendall(json_data.encode())

# Close the socket
client_socket.close()
