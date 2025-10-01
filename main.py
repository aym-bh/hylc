import vlc
import os

videoPath = str(input("enter the video's path: "))

os.system("""hyprctl dispatch exec [fullscreen] 'cvlc --input-repeat=999999 """ + videoPath + "'")
