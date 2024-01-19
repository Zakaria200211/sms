#Decoded By Hso AND Levi: @YIB_31  On: @TYY_313 



foo = False
if foo:
    pass
copyright = '@psh_team'
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon import TelegramClient, sync
from telethon import events
from telethon.tl.custom import Button
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from bs4 import BeautifulSoup
import time
import re
import threading
from time import sleep
import webbrowser
import os
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
webbrowser.open('https://t.me/M_A_M_ll')
khatar = input(F + ' Enter name bot : ')
os.system('clear')
c = requests.session()

def css():
    api_id = '2192036'
    api_hash = '3b86a67fc4e14bd9dcfc2f593e75c841'
    client = TelegramClient('session', api_id, api_hash)
    client.start()
    channel_username = '@' + khatar
    channel_entity = client.get_entity(channel_username)
    client.send_message(khatar, '/start')
    sleep(2)
    print(F + 'بدء التجميع. . .')
    sleep(1)
    mssag = client.get_messages(khatar, 1, **('limit',))
    mssag[0].click(2)
    sleep(10)
    mssag1 = client.get_messages(khatar, 1, **('limit',))
    mssag1[0].click(0)
    sleep(5)
    for ffguf in range(10000):
        sleep(10)
        l = client(GetHistoryRequest(channel_entity, 1, None, 0, 0, 0, 0, 0, **('peer', 'limit', 'offset_date', 'offset_id', 'max_id', 'min_id', 'add_offset', 'hash')))
        j = l.messages[0]
        if j.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            client.send_message('me', '   انتضر عمري خلصت القنوات @CC8CD')
        else:
            url = j.reply_markup.rows[0].buttons[0].url
            
            try:
                
                try:
                    client(JoinChannelRequest(url))
                except:
                bott = url.split('/')[-1]
                client(ImportChatInviteRequest(bott))
                mssag2 = client.get_messages(khatar, 1, **('limit',))
                mssag2[0].click('تحقق', **('text',))
                
                client.send_message('me', '  حضروك عمري تعال راسلني واكلك شسوي @CC8CD')
                
                
                client.disconnect()
                



css()


#Decoded By Hso AND Levi: @YIB_31  On: @TYY_313 

