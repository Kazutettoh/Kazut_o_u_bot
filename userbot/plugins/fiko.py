import asyncio
import random
import logging
from userbot import ALIVE_NAME, bot, CMD_LIST
from userbot.system import command
from platform import uname

from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import MessageIdInvalidError
from userbot import bot
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================

@bot.on(dev_cmd(pattern=f"fiko", outgoing=True))
async def _(event):
    if event.fwd_from:
        return                
    await event.edit(f"{DEFAULTUSER} è il più fiko perché ha l'userbot")
    await asyncio.sleep(3)
    await event.delete()
