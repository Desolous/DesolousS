import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

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
async def nelanbu(ctx):
    await ctx.send(''' Hey Yo {0} ! \n"*sg" İtediğin kişiyi kickle !  (Sadece Yönetici) \n"*sgoç" İstediğin kişiyi banla ! (Sadece Yönetici) \n"*sat" İstediğin kişinin sattığını belirt ! (Herkes)'''.format(ctx.author.mention))

@bot.command(pass_context=True)
async def sat(ctx, member:discord.Member):
    await ctx.send(member.mention + " SATIYOR !!!!")

@bot.command(pass_context = True)
@has_permissions(manage_roles=True, ban_members=True, kick_members=True)
async def sg(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(member.mention + " Yine bekleriz :) Ama önce adam ol.")

@bot.command(pass_context = True)
@has_permissions(manage_roles=True, ban_members=True)
async def sgoç(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(member.mention + " Yolun açık olsun paşam :)")

bot.run("NTkxNzkzODQ2ODA4MDg0NTMx.XRfCpg.X8vN1xfRT-O3IlFWTKW7jHGhLrQ") 

