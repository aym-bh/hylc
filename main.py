import vlc
import time


player = vlc.Instance()

mList = player.media_list_new()


media = player.media_new("miku-purple.3840x2160.mp4")

mList.add_media(media)


media_player = player.media_list_player_new()

media_player.set_media_list(mList)

player.vlm_set_loop("miku-purple.3840x2160", True)

media_player.play()

input()
