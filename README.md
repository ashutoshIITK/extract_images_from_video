# Extract Images From Video using OpenCV
This Python script allows you to extract images from a video files every y seconds.

This script uses OpenCV library for reading the video and writing the frames to disk. Make sure you have OpenCV 3.
# Installation

pip install opencv-python

# Usage

python extract_images.py [input_video_file] [name_of_the_output_image] [x_seconds]

Suppose you want to extract images (myvideo_frames%d.jpg) from a video ('my_video.mp4') every 10 seconds, then the call would be like this:

python extract_images.py my_video.mp4 myvideo_frames 10
