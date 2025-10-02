import vlc
import os

#videoPath = str(input("enter the video's path: "))

videoPath = "/home/aymbh/foss/hylc/cityscape-silhouette.1920x1080.mp4"

os.system("""hyprctl dispatch exec ['float;fullscreen;nofocus'] 'cvlc --input-repeat=999999 """ + videoPath + "'")
