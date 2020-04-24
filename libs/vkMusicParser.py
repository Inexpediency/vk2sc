from bs4 import BeautifulSoup
import requests as req
import re


class VkParser:
    @staticmethod
    def parsing(playlist_link):
        resp = req.get(playlist_link)
        soup = BeautifulSoup(resp.text, features="html.parser")

        # Get music list
        music_list = re.split(r'audioPlaylistSnippet__list', str(soup))[1]
        music_list = re.split(r'data-audio', music_list)[1:-1]
        music_list = str(music_list)

        with open("guru99.txt", "w+", encoding="utf8") as f:
            f.write(music_list)
