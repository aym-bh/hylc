import vlc
import os

# needs hyprwinwrap


#videoPath = str(input("enter the video's path: "))

videoPath = "/home/aymbh/foss/hylc/cityscape-silhouette.1920x1080.mp4"

os.system("""hyprctl dispatch exec ['float;nofocus;pin;monitor HDMI-A-2;size 100% 100%;move 0 0;bordersize 0;rounding 0;tag +cute'] 'cvlc --input-repeat=999999 """ + videoPath + "'")
