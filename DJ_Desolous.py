import discord
from discord.ext.commands import Bot
from discord.ext import commands

bot = discord.Client()
bot_prefix="*"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    print ("Çalıştırılıyor")
    activity = discord.Game(name="Duygularımla")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print ("Aktif")

@bot.command(pass_context=True)
async def sat(ctx, member:discord.Member):
    await ctx.send(member.mention + " SATIYOR !!!!")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="boşlar")
    await channel.send(member.mention + " Hoşgeldin Paşam !")


@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="boşlar")
    await channel.send(member.mention + " Hop Hemşerim Nereye ?")

bot.run("NTk2MDAyNzA3MDYwMjkzNjQz.XR4Yyg.c3M8Q-Uvc6X0TGKI_IZaM0k5wFE") 

