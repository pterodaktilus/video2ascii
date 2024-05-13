
import sys 
import os
import cv2
import time as t
from numpy import array,round,zeros

chars = array(list("""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.  """)[::-1])
def translate(val):
    val = round(val/255*(len(chars)-1)).astype(int)
    return chars[val]
    
cam = cv2.VideoCapture(sys.argv[1]) 
length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
w = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames = zeros((length, h,w), dtype=str)
i = 0
while(True): 
    # reading from frame 
    ret,frame = cam.read() 
    
    if ret: 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames[i]=(translate(frame))
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        num = "{:.2f}".format(i/(length-1)*100)
        sys.stdout.write(f"translation: {num}%")
        sys.stdout.flush()
        i+=1
    else:
        break
input("\nPress Enter to continue...")
size = frames.shape
for i in range(size[0]):
    for j in range(size[1]):
        sys.stdout.write("".join(frames[i][j].tolist())+"\n")
        sys.stdout.flush()
    t.sleep(1/60)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
