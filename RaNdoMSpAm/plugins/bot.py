import asyncio
import os
from pathlib import Path
import base64
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from RaNdoMSpAm import random, random2, random3, random4, random5 , random6, random7, random8, random9, random10, random11, random12, random13, random14, random15, random16, random17, random18, random19, random20, random21, random22, random23, random24, random25, random26, random27, random28, random29, random30, random31, random32, random33, random34, random35, random36, random37, random38, random39, random40, DEV
from .. import CMD_HNDLR as hl
from telethon import events
from telethon.tl.types import Channel, Chat, InputPhoto, User


#name    
    
@random.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random2.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random3.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random4.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random5.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random6.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random7.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random8.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random9.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random10.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random11.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random12.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random13.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random14.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random15.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random16.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random17.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random18.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random19.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random20.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random21.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random22.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random23.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random24.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random25.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random26.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random27.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random28.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random29.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random30.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random31.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random32.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random33.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random34.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random35.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random36.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random37.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random38.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random39.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@random40.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
async def name(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗡𝗔𝗠𝗘\n\nCommand:\n\n.setname <Message to change name of spam ids>"
    if e.sender_id in DEV:
        names = e.text.split(" ", 1)
        randomo = names[1]
        if len(e.text) > 5:
            firstname = randomoeL
            text = "Changing Name..."
            try:
                await e.client(functions.account.UpdateProfileRequest(first_name=firstname))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await event.edit("Changed name successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

#bio 
            
@random.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random2.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random3.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random4.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random5.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random6.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random7.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random8.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random9.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random10.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random11.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random12.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random13.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random14.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random15.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random16.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random17.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random18.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random19.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random20.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random21.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random22.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random23.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random24.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random25.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random26.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random27.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random28.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random29.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random30.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random31.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random32.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random33.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random34.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random35.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random36.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random37.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random38.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random39.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@random40.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
async def _(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗕𝗜𝗢\n\nCommand:\n\n.setbio <Message to change name of spam ids>"
    if e.sender_id in DEV:
        fukyou = e.text.split(" ", 1)
        message = fukyou[1]
        if len(e.text) > 5:
            bio = message
            text = "Changing Bio..."
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Changed bio successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )         
        

# statss                   
            
@random.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random2.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random3.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random4.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random5.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random6.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random7.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random8.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random9.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random10.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random11.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random12.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random13.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random14.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random15.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random16.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random17.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random18.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random19.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random20.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random21.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random22.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random23.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random24.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random25.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random26.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random27.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random28.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random29.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random30.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random31.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random32.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random33.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random34.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random35.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random36.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random37.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random38.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random39.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@random40.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
async def stats(event):
   u = 0
   g = 0
   c = 0
   bc = 0
   b = 0
   randomoel = ""
   if event.sender_id in DEV:    
        await event.delete()
        event = await event.reply("__Processing__.....")
       # await event.edit("`Processing..`")
        dialogs = await event.client.get_dialogs(limit=None, ignore_migrated=True)
        for d in dialogs:
            currrent_entity = d.entity
            if isinstance(currrent_entity, User):
                if currrent_entity.bot:
                    b += 1
                else:
                    u += 1
            elif isinstance(currrent_entity, Chat):
                g += 1
            elif isinstance(currrent_entity, Channel):
                if currrent_entity.broadcast:
                    bc += 1
                else:
                    c += 1
            else:
                print(d)
         
        randomoel += f"🔻 **HERE IS YOUR RaNdoMSpAm STATS** 🔻\n\n"
        randomoel += f"`Users:`\t**{u}**\n"
        randomoel += f"`Groups:`\t**{g}**\n"
        randomoel += f"`Super Groups:`\t**{c}**\n"
        randomoel += f"`Channels:`\t**{bc}**\n"
        randomoel += f"`Bots:`\t**{b}**"
        await event.edit(randomoel)    
    
    
    
