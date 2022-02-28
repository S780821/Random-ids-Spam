import asyncio
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from RaNdoMSpAm import random, random2, random3, random4, random5 , random6, random7, random8, random9, random10, random11, random12, random13, random14, random15, random16, random17, random18, random19, random20, random21, random22, random23, random24, random25, random26, random27, random28, random29, random30, random31, random32, random33, random34, random35, random36, random37, random38, random39, random40, SUDO_USERS
from resources.data import randomX
from .. import CMD_HNDLR as hl
  
    
@random.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random2.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random3.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random4.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random5.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random6.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random7.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random8.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random9.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random10.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random11.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random12.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random13.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random14.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random15.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random16.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random17.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random18.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random19.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random20.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random21.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random22.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random23.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random24.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random25.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random26.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random27.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random28.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random29.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random30.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random31.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random32.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random33.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random34.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random35.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random36.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random37.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random38.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random39.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@random40.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
async def _(e):
    usage = "**Module Name = Abuse**\n\nCommand:\n\n .gali <Username of User>\n\nit will continuously abuse until you restart!!."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        random = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(random) == 1:
            user = str(random[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in randomX:
                text = f"I can't abuse @randomX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                name = f"[{c}](tg://user?id={g})"
                caption1 =f"{name} GAND FATT GYII KYA HIJRE KI OLAAD"
                caption2 =f"{name} **RANDI KE PILLLE**"
                caption3 =f" {name} 𝑪𝑯𝑯𝑯𝑯𝑯𝑼𝑼𝑼𝑼𝑼𝑫𝑫𝑫𝑫 𝑮𝒀𝑨𝑨𝑨𝑨𝑨𝑨𝑨 𝑳𝑶𝑽𝑽𝑽𝑽𝑽𝑫𝑫𝑬𝑬 𝑻𝑼𝑼𝑼𝑼"
                caption4 =f" {name} 𝕋𝕖𝕣𝕚 𝕄𝕒𝕒 𝕂𝕚 𝕏𝕙𝕠𝕥 𝕓𝕒𝕕𝕙𝕧𝕖"
                caption5 =f"{name} **ISKE MAAKI CHUTT LELO FREE FULL NIGHT**"
                caption6 =f" {name} __TERE MAAKI CHUTT MASTT SOFT SOFT HE__ 🤤"
                caption7 =f"# {name} TERE MAAKI CHUT ME MERAA LUNDD"
                caption8 =f"{name} **RAANDD KAA PILLAAA**"
                caption9 =f"{name} 𝙄𝙎𝙆𝙄 𝘽𝙃𝙀𝙉 𝙈𝙀𝙍𝘼 𝙇𝙐𝙉𝘿 𝘾𝙃𝙊𝙊𝙎𝙏𝙄𝙄 𝙃E"
                caption10 =f"{name} __AGAYA SWADH__"
                caption11 =f"{name} **TERI MAAA**"
                caption12 =f"**MERE SE**"
                caption13 =f"**Rozz CHUDTII**"
                caption14 =f"__Haiii__"
                caption15 =f"{name} TERE BHEN KO CHODU"
                caption16 =f"🆃🅰🅿🅰"
                caption17 =f"🆃🅰🅿"
                caption18 =f"🆃🅰🅿🅰"
                caption18 =f"🆃🅰🅿"
                caption20 =f"__NON STOP__"
                caption21 =f"{name} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗠𝗘𝗥𝗘 𝗟𝗨𝗡𝗗 𝗟𝗘 𝗡𝗔𝗖𝗛𝗧𝗜 𝗛𝗘"
                caption22 =f"🤤"
                caption23 =f"{name} __TERI MAA MST ARAAM DETI HE__🤤🤤"
                caption24 =f"{name} __KE BHEN KI CHUT LELO FULL NIGHT FREEE__"
                caption25 =f"{name} __KI BHEN RANDIII__"
                caption26 =f"{name} __ISKE BHEN MST MARI RANDI__ 🤤🤤"
                caption27 =f"😂🖕🤣"
                caption28 =f"😂"
                caption29 =f"__EK RUPAY KI PEPSI {name} KI NAANI SEXYY__"
                caption30 =f"{name} **ISKI BHEN MERI PERSONAL HE MENE BOHOT CHODAA HE USKO__ \n\n __DM {name} FOR PERSONAL RANDI__"
                fuk = e.chat_id
                async with e.client.action(fuk, "typing"):
                        await e.client.send_message(fuk, caption1)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption2)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption3)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption4)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption5)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption6)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption7)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption8)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption9)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption10)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption11)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption12)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption13)
                        await asyncio.sleep(0.4)
                        await e.client.send_message(fuk, caption14)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption15)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption16)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption17)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption18)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption19)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption20)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption21)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption22)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption23)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption24)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption25)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption26)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption27)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption28)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption29)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption30)
                        await asyncio.sleep(0.3)

        else:
             await e.reply(usage)
