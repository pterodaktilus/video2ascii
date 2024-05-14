
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
time = int(cam.get(cv2.CAP_PROP_POS_MSEC))
w = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames = zeros((length, h,w), dtype=str)
i = 0
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
while(True): 
    # reading from frame 
    ret,frame = cam.read() 
    
    if ret: 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames[i]=(translate(frame))
        
        num = "{:.2f}".format(i/(length-1)*100)
        sys.stdout.write(f"translation: {num}%")
        sys.stdout.write("\033[0;0H")
        sys.stdout.flush()
        i+=1
    else:
        break
input("\nPress Enter to continue...")
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
size = frames.shape
for i in range(size[0]):
    string = ""
    for j in range(size[1]):
        string+="".join(frames[i][j].tolist())+"\n"
    sys.stdout.write(string)
    sys.stdout.flush()
    t.sleep(length/time)
    sys.stdout.write("\033[0;0H")
    sys.stdout.flush()

