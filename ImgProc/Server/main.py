#### AY RANK 8EER ZERO ####

import json
import cv2
import socket
import numpy as np

sockk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

sockk.bind((host,port))

sockk.listen()

client_sockk, addr = sockk.accept()

jsonData = b""
while True:
    packet = client_sockk.recv(1024)
    if not packet:
        break
    jsonData += packet
    
    
data = json.loads(jsonData.decode())

img_array = np.frombuffer(bytes(data['image'], 'utf-8'), dtype=np.uint8)

img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
print(img)
cv2.imwrite("./recvimg.jpg", img)