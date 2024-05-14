import sys 
import os
import cv2
import time as t
from numpy import array, round, zeros

# Define the characters used for ASCII art
chars = array(list("""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.  """)[::-1])

# Function to translate pixel values to ASCII characters
def translate(val):
    val = round(val/255*(len(chars)-1)).astype(int)
    return chars[val]

# Open the video file specified as a command line argument
cam = cv2.VideoCapture(sys.argv[1]) 

# Get video properties
length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cam.get(cv2.CAP_PROP_FPS)  
w = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create an array to store the ASCII frames
frames = zeros((length, h, w), dtype=str)

i = 0

# Clear the console screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

while(True): 
    # Read a frame from the video
    ret, frame = cam.read() 
    
    if ret: 
        # Convert the frame to grayscale
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Translate the pixel values to ASCII characters
        frames[i] = translate(frame)
        
        # Print the translation progress
        num = "{:.2f}".format(i/(length-1)*100)
        sys.stdout.write(f"translation: {num}%")
        sys.stdout.write("\033[0;0H")
        sys.stdout.flush()
        
        i += 1
    else:
        break

# Wait for user input before continuing
input("\nPress Enter to continue...")

# Clear the console screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# Get the size of the frames array
size = frames.shape

# Display the ASCII frames
for i in range(size[0]):
    string = ""
    for j in range(size[1]):
        string += "".join(frames[i][j].tolist()) + "\n"
    sys.stdout.write(string)
    sys.stdout.flush()
    
    # Delay between frames based on the video's FPS
    t.sleep(1/fps)
    
    sys.stdout.write("\033[0;0H")
    sys.stdout.flush()
