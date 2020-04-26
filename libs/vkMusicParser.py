from bs4 import BeautifulSoup
import json
from pprint import pprint
import requests as req
import json
from pprint import pprint
import re
import subprocess


class VkParser:
    @staticmethod
    def parsing(playlist_link):

        curl_command = f"""curl 'https://vk.com/al_audio.php?act=load_section' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://vk.com' -H 'Referer: {playlist_link}' -H 'Connection: keep-alive' -H 'Cookie: remixlang=0; remixstid=2082697607_N5XMiuUoDYMLRpStW2uyOnHHggeo9q8cgVstj95ZEfz; tmr_reqNum=3; tmr_lvid=8773e81a24e83e889c157505b59dd19a; tmr_lvidTS=1581252574305; remixlhk=02a19a865ecc8aaf7d; remixflash=0.0.0; remixscreen_width=1680; remixscreen_height=1050; remixscreen_dpr=1; remixscreen_depth=24; remixscreen_orient=1; remixscreen_winzoom=1; remixgp=ee4a633e74cf9eaf84304904a2a5cdda; remixdt=0; tmr_detect=0%7C1587844121187' -H 'Cache-Control: max-age=0' -H 'TE: Trailers' --data 'access_hash=&al=1&claim=0&context=&from_id=378560088&is_loading_all=1&is_preload=0&offset=0&owner_id=378560088&playlist_id=167&type=playlist' --compressed > music_list.json"""
        cmd_command = 'curl "https://vk.com/al_audio.php?act=load_section" -H "authority: vk.com" -H "origin: https://vk.com" -H "x-requested-with: XMLHttpRequest" -H "sec-fetch-dest: empty" -H "save-data: on" -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.2.238 Yowser/2.5 Safari/537.36" -H "content-type: application/x-www-form-urlencoded" -H "accept: */*" -H "sec-fetch-site: same-origin" -H "sec-fetch-mode: cors" -H "referer: https://vk.com/ythosa?z=audio_playlist378560088_167" -H "accept-language: ru,en;q=0.9" -H "cookie: remixlang=0; remixscreen_depth=24; remixusid=MWQzMDcxNTVlYjU1M2I0NzEzYjljZDNm; _ga=GA1.2.214140627.1564665827; remixfeed=*.*.*.*.*.fr^%^2Cpr^%^2Cev^%^2Ccm.*.photos^%^2Cvideos^%^2Cfriends^%^2Cgroups^%^2Cpodcasts^%^2Cti2019; tmr_lvid=3b8f0057abc8f3350e922bd8456d0bbe; tmr_lvidTS=1572691072803; remixstid=156810411_TLwHsv5gYEkuh7aLgEZsXdzTb5xmtjXjTF6FD892nOT; remixrefkey=b45f45ce4fb1e72844; remixflash=32.0.0; remixscreen_width=1680; remixscreen_height=1050; remixscreen_dpr=1; remixscreen_orient=1; remixgp=dc81536be1c9765cecd29bb913aaa920; remixbdr=0; remixua=37^%^7C-1^%^7C131^%^7C1831361832; remixscreen_winzoom=1; remixdt=-10800; remixlhk=54d1677abdfb99a873; remixsts=^%^7B^%^22data^%^22^%^3A^%^5B^%^5B1587923453^%^2C^%^22counters_check^%^22^%^2C1^%^5D^%^5D^%^2C^%^22uniqueId^%^22^%^3A898455046^%^7D; tmr_detect=1^%^7C1587923453397; tmr_reqNum=3630" --data "access_hash=^&al=1^&claim=0^&context=^&from_id=378560088^&is_loading_all=1^&is_preload=0^&offset=0^&owner_id=378560088^&playlist_id=167^&type=playlist" > music_list.json'

        music_list = subprocess.run(cmd_command, shell=True)

        if music_list.returncode != 0:
            exit('It was some evil there :( Try again :(')

        with open('music_list.json', 'r', encoding='cp1251') as f:
            data = json.load(f)

        music_list = data.get('payload')[1][0]
        
        pprint(music_list)        
