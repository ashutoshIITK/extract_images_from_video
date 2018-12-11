
# coding: utf-8
# The script is written by Ashutosh Kumar. Contact here: askumar.iitk@gmail.com


#Importing all necessary libraries here

import cv2
import sys

# Writing images to disk function

def write_frames(vidcap, outfile, fps, second):
    success = True
    counter = 0
    while success:
        success, frame = vidcap.read()
        if counter % (second * fps) == 0:
            cv2.imwrite('{}%d.jpg'.format(outfile) % counter, frame)
            print('Writing image to disk')
        counter += 1
        
if __name__ == "__main__":
    try:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        second = float(sys.argv[3])
    except:
        print("Wrong arguments. Please see the usage of the script.")
        sys.exit()
    vidcap = cv2.VideoCapture(infile)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    write_frames(vidcap, outfile, fps, second)

