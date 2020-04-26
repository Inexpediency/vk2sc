from bs4 import BeautifulSoup
import requests as req
import re
import subprocess

class VkParser:
    @staticmethod
    def parsing(playlist_link):

        command = f"""curl 'https://vk.com/al_audio.php?act=load_section' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://vk.com' -H 'Referer: {playlist_link}' -H 'Connection: keep-alive' -H 'Cookie: remixlang=0; remixstid=2082697607_N5XMiuUoDYMLRpStW2uyOnHHggeo9q8cgVstj95ZEfz; tmr_reqNum=3; tmr_lvid=8773e81a24e83e889c157505b59dd19a; tmr_lvidTS=1581252574305; remixlhk=02a19a865ecc8aaf7d; remixflash=0.0.0; remixscreen_width=1680; remixscreen_height=1050; remixscreen_dpr=1; remixscreen_depth=24; remixscreen_orient=1; remixscreen_winzoom=1; remixgp=ee4a633e74cf9eaf84304904a2a5cdda; remixdt=0; tmr_detect=0%7C1587844121187' -H 'Cache-Control: max-age=0' -H 'TE: Trailers' --data 'access_hash=&al=1&claim=0&context=&from_id=378560088&is_loading_all=1&is_preload=0&offset=0&owner_id=378560088&playlist_id=167&type=playlist' --compressed > music_list.json"""

        music_list = subprocess.run(command, shell=True)
