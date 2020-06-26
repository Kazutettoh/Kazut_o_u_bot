@bot.on(dev_cmd(pattern=f"check", outgoing=True))
async def _(event):
    if event.fwd_from:
        return                
    await event.edit("L'userbot è Online✅")
    await asyncio.sleep(3)
    await event.delete()
