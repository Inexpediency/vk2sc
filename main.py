#! python3

from libs.tokens import VK_PLAYLIST_LINK

from libs.vkMusicParser import VkParser

music_list = VkParser.parsing(VK_PLAYLIST_LINK)

with open('playlist.txt', 'w') as f:
    f.write(music_list)
