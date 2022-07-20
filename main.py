import asyncio
import downloader, forwarder
import keyboard
import os
from configparser import ConfigParser
config_object = ConfigParser()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

f  = open("ascii.txt", "r")
ascii = "".join(f.readlines())

def menudraw():
    print(colorText(ascii))

menudraw()


config_object.read("config.ini")


try:
    userinfo = config_object["LOGIN"]
    api_id = userinfo["api_id"]
    api_hash = userinfo["api_hash"]
except:

    config_object["LOGIN"] = {
        "api_id": 00000,
        "api_hash": "hash32"
    }

    with open('config.ini', 'w') as conf:
        config_object.write(conf)

def downloaderMenu():
    print(colorText("[[yellow]]Download channel documents to downloads folder with channel id.[[white]]"))
    tg_ch_id = int(input("[TELEGRAM_CHANNEL_ID]>"))
    print(colorText("[[red]]Download starting...[[white]]"))
    asyncio.run(downloader.fileDownloader(tg_ch_id, api_id, api_hash))
    main()


def forwarderMenu():
    print(colorText("[[yellow]]Copy channel messages to another channel with channel ids.[[white]]"))
    tg_trgt_ch_id = int(input("[TELEGRAM_TARGET_CHANNEL_ID]>"))
    tg_cpyto_ch_id = int(input("[TELEGRAM_COPYTO_CHANNEL_ID]>"))
    print(colorText("[[red]]Forward starting...[[white]]"))
    asyncio.run(forwarder.forwarder(tg_trgt_ch_id, tg_cpyto_ch_id, api_id, api_hash))
    main()



def main():
    print(colorText("[[green]][C] [[yellow]]Copy channel messages[[white]]"))
    print(colorText("[[green]][D] [[yellow]]Download channel documents[[white]]"))
    print(">")
    while True:
        if keyboard.is_pressed("D"):
            clear()
            menudraw()

            downloaderMenu()
            break
        if keyboard.is_pressed("C"):
            clear()
            menudraw()

            forwarderMenu()

            break

main()


