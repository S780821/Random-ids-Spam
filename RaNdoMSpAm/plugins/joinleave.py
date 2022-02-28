import asyncio
from RaNdoMSpAm import random, random2, random3, random4, random5 , random6, random7, random8, random9, random10, random11, random12, random13, random14, random15, random16, random17, random18, random19, random20, random21, random22, random23, random24, random25, random26, random27, random28, random29, random30, random31, random32, random33, random34, random35, random36, random37, random38, random39, random40, SUDO_USERS
from .. import CMD_HNDLR as hl
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events
import os
import random
import sys


@random.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random2.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random3.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random4.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random5.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random6.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random7.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random8.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random9.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random10.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random11.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random12.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random13.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random14.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random15.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random16.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random17.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random18.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random19.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random20.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random21.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random22.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random23.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random24.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random25.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random26.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random27.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random28.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random29.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random30.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random31.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random32.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random33.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random34.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random35.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random36.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random37.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random38.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random39.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@random40.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SUDO_USERS:
        randomoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = randomoel[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Joined Successfully ✅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@random.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random2.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random3.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random4.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random5.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random6.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random7.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random8.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random9.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random10.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random11.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random12.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random13.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random14.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random15.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random16.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random17.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random18.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random19.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random20.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random21.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random22.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random23.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random24.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random25.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random26.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random27.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random28.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random29.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random30.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random31.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random32.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random33.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random34.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random35.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random36.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random37.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random38.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random39.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@random40.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/abcdefghijklmsnob\n\n.pjoin abcdefghijklmsnob"
    if e.sender_id in SUDO_USERS:
        randomoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = randomoel[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Joined Successfully (Private Group/channel) ✅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



#leave 
@random.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random11.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random12.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random13.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random14.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random15.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random16.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random17.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random18.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random19.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random20.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random21.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random22.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random23.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random24.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random25.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random26.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random27.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random28.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random29.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random30.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random31.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random32.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random33.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random34.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random35.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random36.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random37.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random38.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random39.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@random40.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SUDO_USERS:
        randomoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = randomoel[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left ☑️")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )   
