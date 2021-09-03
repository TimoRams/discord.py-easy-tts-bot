import asyncio as asyncio
import discord
from discord.ext import commands
from gtts import gTTS
from mutagen.mp3 import MP3
import os

bot = commands.Bot(command_prefix='.', description="This is Easy tts bot")
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)
@bot.command()
async def tts(ctx, *, ttsword):
    try:
        os.remove("output.mp3")
    exept:
        language = 'de'
    language = 'de'
    output = gTTS(text=ttsword, lang=language, slow=False)
    output.save("output.mp3")
    audio = MP3("output.mp3")
    guild = ctx.guild
    voice = await ctx.message.author.voice.channel.connect()
    voice.play(discord.FFmpegPCMAudio('output.mp3'))
    counter = 0
    duration = audio.info.length  # In seconds
    while not counter >= duration:
        await asyncio.sleep(1)
        counter = counter + 1
    await voice.disconnect()
# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/TimoRams"))
    print('My Ready is Body')
bot.run('TOKEN')
