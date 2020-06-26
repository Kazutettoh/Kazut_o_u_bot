import asyncio
from telethon import events
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.system import dev_cmd

@bot.on(dev_cmd("lol ?(.*)", outgoing=True))
async def lol(e):
    await e.edit(
"\n██╗░░░░░░█████╗░██╗░░░░░"
"\n██║░░░░░██╔══██╗██║░░░░░"
"\n██║░░░░░██║░░██║██║░░░░░"
"\n██║░░░░░██║░░██║██║░░░░░"
"\n███████╗╚█████╔╝███████╗"
"\n╚══════╝░╚════╝░╚══════╝")
 
 @bot.on(dev_cmd("f ?(.*)", outgoing=True))
async def f(e):
    await e.edit(
"\n┏━━━┓"
"\n┃┏━━┛"
"\n┃┗━━┓"
"\n┃┏━━┛"
"\n┃┃   "
"\n┗┛   ")             
