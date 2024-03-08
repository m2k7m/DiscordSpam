import info,json,random,sys,subprocess
from discord.ext import tasks,commands

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('git+https://github.com/dolfies/discord.py-self.git')

bot = commands.Bot(command_prefix='!L')

with open('languages.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')
    leveling.start()

if info.TIME is None or info.TIME < 0:
      print('Check TIME in info.py')

@tasks.loop(seconds=info.TIME)
async def leveling():
    channel = bot.get_channel(info.CHANNELID)
    if channel is None:
       print('Channel ID not Found')
       return
    if 'ar' in info.LANGUAGE :
     values = data['ar']
     if isinstance(values, list):
         random_ar = random.choice(values)
         await channel.send(content=random_ar)
    elif 'en' in info.LANGUAGE :
     values = data['en']
     if isinstance(values, list):
         random_en = random.choice(values)
         await channel.send(content=random_en)
    else:
       await channel.send(content=info.CONTANT)

bot.run(info.TOKEN)
