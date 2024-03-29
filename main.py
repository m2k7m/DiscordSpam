import info,json,random,sys,subprocess,asyncio
from discord.ext import tasks,commands
from random import randint

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('git+https://github.com/dolfies/discord.py-self.git')

bot = commands.Bot(command_prefix='!')
ban = []

with open('languages.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')
    leveling.start()

@bot.event
async def autoReaction(reaction, user):
    if reaction.emoji == "🎉":
        if user.bot:
            await asyncio.sleep(round(randint(5,10)))
            await reaction.message.add_reaction("🎉")
            ban.append(reaction.message.id)

if info.TIME is None or info.TIME < 0:
    print('Check TIME in info.py')
    exit()

@tasks.loop(seconds=info.TIME)
async def leveling():
    channel = bot.get_channel(info.CHANNELID)
    if channel is None:
       print('Channel ID not Found\nNote: Type Channel ID without ( " ) Please')
       return
    if 'ar' in info.LANGUAGE :
       values = data['ar']
       if isinstance(values, list):
        random_ar = random.choice(values)
        message = await channel.send(content=random_ar)
    elif 'en' in info.LANGUAGE :
       values = data['en']
       if isinstance(values, list):
        random_en = random.choice(values)
        message = await channel.send(content=random_en)
    else:
       message = await channel.send(content=info.CONTANT)
    if info.DEL == True:
        await message.delete(delay=5)

bot.run(info.TOKEN)
