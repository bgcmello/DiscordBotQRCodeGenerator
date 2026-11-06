# pip install discord.py qrcode[pil]

import io
import discord
from discord.ext import commands
import qrcode

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
@commands.has_permissions(administrator=True)
async def qr(ctx, *, text: str):
  buf = io.BytesIO()
  qrcode.make(text).save(buf, "PNG")
  buf.seek(0)
  await ctx.send(file=discord.File(buf, "qr.png"))


bot.run("")