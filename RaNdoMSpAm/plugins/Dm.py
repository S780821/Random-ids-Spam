import random
import asyncio
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from resources.data import random, RAID
from RaNdoMSpAm import random, random2, random3, random4, random5 , random6, random7, random8, random9, random10, random11, random12, random13, random14, random15, random16, random17, random18, random19, random20, random21, random22, random23, random24, random25, random26, random27, random28, random29, random30, random31, random32, random33, random34, random35, random36, random37, random38, random39, random40, SUDO_USERS
from .. import CMD_HNDLR as hl


@random.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random2.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random3.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random4.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random5.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random6.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random7.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random8.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random9.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random10.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random11.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random12.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random13.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random14.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random15.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random16.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random17.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random18.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random19.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random20.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random21.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random22.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random23.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random24.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random25.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random26.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random27.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random28.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random29.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random30.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random31.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random32.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random33.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random34.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random35.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random36.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random37.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random38.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random39.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@random40.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
async def _(e):   
    usage = "**MODULE NAME** : **DM**\n\n command: \n\n .dm <username> <massage> \n .dm <reply to the use> <massage>"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        randomoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(randomoeL) == 2:
            user = str(randomoeL[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in random:
                text = f"I can't Dm to @random's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:            
                 message = str(randomoeL[1])
                 await e.reply("🔸Message Delivered🔸")
                 await e.client.send_message(g, message)
                 await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in random:
                text = f"I can't Dm to @random's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(randomoeL[0])
                await e.reply("🔸 Message Delivered 🔸")
                await e.client.send_message(g, message)
                await asyncio.sleep(0.3)

        else:
             await e.reply(usage)


@random.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random2.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random3.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random4.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random5.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random6.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random7.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random8.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random9.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random10.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random11.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random12.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random13.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random14.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random15.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random16.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random17.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random18.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random19.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random20.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random21.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random22.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random23.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random24.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random25.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random26.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random27.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random28.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random29.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random30.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random31.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random32.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random33.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random34.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random35.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random36.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random37.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random38.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random39.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@random40.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
async def dmraid(e):
    usage = "**MODULE NAME** : **DM RAID**\n\n command: \n\n .dmraid <count> <username> \n .dmraid <reply to the use> <massage>"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        randomoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(randomoeL) == 2:
            user = str(randomoeL[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in random:
                text = f"I can't raid on @random's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(randomoeL[0])
                await e.reply("⚜️ Dm Raid Strated Successfully ⚜️")
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{reply}"
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, caption)
                        await asyncio.sleep(0.4)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in random:
                text = f"I can't raid on @random's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(randomoeL[0])
                await e.reply("⚜️ Dm Raid Strated Successfully!! ⚜️")
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{reply}"
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)
