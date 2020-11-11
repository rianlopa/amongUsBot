import discord
from discord.ext import commands, tasks
from PIL import ImageGrab
import pytesseract

client = commands.Bot(command_prefix = '.')

global leader
leader = None

@client.event
async def on_ready():
    print("hello")
    #change_voice.start()

@client.command()
async def lider(ctx):
    global leader

    if leader == None:
        leader = ctx.author
        await ctx.send(f"```[*] Host connected: {ctx.author.name}```")

#@tasks.loop(seconds=1)
# async def change_voice():

@client.command()
async def inicio(ctx):
    global leader
    
    previous = True

    while True:
        img = ImageGrab.grab(bbox=(400,-30,2000,600))

        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
        word = pytesseract.image_to_string(img)

        imp = 'Impostor'

        if(imp in word and previous==False):
            for member in list(client.get_channel(leader.voice.channel.id).members):
                await member.edit(mute = False)
            previous = True

        if(imp not in word and previous==True):
            for member in list(client.get_channel(leader.voice.channel.id).members):
                await member.edit(mute = True)
            previous = False


'''@client.command()
async def mutear(ctx):
    global leader
    for member in list(client.get_channel(leader.voice.channel.id).members):
        await member.edit(mute = True)
'''
@client.command()
async def desmutear(ctx):
    global leader
    for member in list(client.get_channel(leader.voice.channel.id).members):
        await member.edit(mute = False)

client.run('Aqui debe ir el tocken generado de discord dev')