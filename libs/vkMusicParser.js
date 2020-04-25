const fetch = require('node-fetch')
const fs = require('fs')
const {VK_PLAYLIST_LINK} = require('./tokens')

async function get_music_list() {
    data = await fetch("https://vk.com/al_audio.php?act=load_section", {
            "headers": {
                "accept": "*/*",
                "accept-language": "ru,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest",
                "cookie": "remixscreen_depth=24; remixdt=0; tmr_lvid=1c6be03c656f7bec3dfdf83c6a4de43c; tmr_lvidTS=1555004173664; remixlang=0; remixstid=1510797190_i27zMuHUHEUszKlsyJTJtep0Wlyrs0TmowA4rh2yK7o; remixflash=32.0.0; remixusid=OGNhNmVhMzYyOTIyODY0NWMxYjk2NGNj; remixscreen_width=1366; remixscreen_height=768; remixua=37%7C-1%7C131%7C1831361832; remixscreen_dpr=1.100000023841858; remixscreen_orient=1; remixgp=cf56754f1ca131a0c02bc5b8959e93ba; remixseenads=0; remixrefkey=a6827150ef91b10e0f; remixbdr=1; remixlhk=2ed2ee33472d1012f2; remixscreen_winzoom=2.47; tmr_detect=0%7C1587803688452; remixcurr_audio=378560088_456240438; remixsts=%7B%22data%22%3A%5B%5B1587803983%2C%22counters_check%22%2C1%5D%5D%2C%22uniqueId%22%3A509933269%7D; tmr_reqNum=68"
            },
            "referrer": `${VK_PLAYLIST_LINK}`,
            "referrerPolicy": "no-referrer-when-downgrade",
            "body": "access_hash=&al=1&claim=0&context=&from_id=378560088&is_loading_all=1&is_preload=0&offset=0&owner_id=378560088&playlist_id=167&type=playlist",
            "method": "POST",
            "mode": "cors"
        })
    fs.writeFileSync('../guru99.txt', data, 'utf8')
}

module.exports = get_music_list
