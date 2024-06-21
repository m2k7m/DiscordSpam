import json,random,asyncio,yaml
from discord import *
from discord.ext import tasks,commands
from random import randint

bot = commands.Bot(command_prefix='!')

with open("config.yml","r",encoding="utf8") as f:
    config = yaml.safe_load(f)

with open('languages.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

if config["TIME"] is None or config["TIME"] < 0:
    input('Check TIME in config.yml')
    exit()

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')
    leveling.start()

@bot.event
async def autoReaction(reaction:Reaction, user:User):
    if reaction.emoji == "🎉":
        if user.bot:
            await asyncio.sleep(round(randint(5,10)))
            await reaction.message.add_reaction("🎉")

@tasks.loop(seconds=config["TIME"])
async def leveling():
    channel = bot.get_channel(config["CHANNELID"])
    if channel is None:
       input('Channel ID not Found\nNote: Type Channel ID without ( " ) Please')
       exit()
    if config["LANGUAGE"] == "ar" :
       values = data['ar']
       if isinstance(values, list):
        random_ar = random.choice(values)
        message = await channel.send(random_ar)
    elif config["LANGUAGE"] == "en" :
       values = data['en']
       if isinstance(values, list):
        random_en = random.choice(values)
        message = await channel.send(random_en)
    else:
       message = await channel.send(config["CONTANT"])
    if config["DEL"] == True or config["DEL"] is True:
        await message.delete(delay=5)

@bot.event
async def on_message(message:Message):
    if message.author != bot.user:
        return
    elif message.content.startswith('!v'):
        channel_id = int(message.content.split(' ')[1])
        c = bot.get_channel(channel_id)
        if c:
            if bot.voice_clients:
                await bot.voice_clients[0].disconnect()
            await c.connect(self_deaf=True,self_mute=True)
            await message.edit(content=f"Connected to **{c.name}**.")
        else:
            await message.edit(content="Invalid channel ID. Please provide a valid voice channel ID.")
    elif message.content == '!l':
        if bot.voice_clients:
            vc = bot.voice_clients[0]
            await vc.disconnect()
            await message.edit(content=f"Disconnected from **{vc.channel.name}**.")
        else:
            await message.edit(content="Not connected to any voice channel.")

bot.run(config["TOKEN"])
