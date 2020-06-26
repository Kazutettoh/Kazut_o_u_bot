import asyncio
import random
import logging

from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import MessageIdInvalidError
from userbot import bot
from userbot.system import dev_cmd

@bot.on(dev_cmd(pattern=f"check", outgoing=True))
async def _(event):
    if event.fwd_from:
        return                
    await event.edit("L'userbot è Online✅")
    await asyncio.sleep(3)
    await event.delete()
