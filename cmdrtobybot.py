import discord
intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
intents.messages = True
import discord.utils
import os
import logging
from discord import *
from discord.ext import commands, tasks
from itertools import cycle
geese = os.environ.get('BOT_TOKEN')
# all stage 1 events are in this file, extensions are where functions are called from
#test comment for Xcode pushes to github

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)





client = commands.Bot(command_prefix = '>' , intents = intents)
status = cycle(['Minecraft'])

print('Loading extensions.....')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_connect():
    print ('Connecting...')
@client.event
async def on_ready():
    print('Setting status....')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Minecraft'))
    change_status.start()
    print('-------------------------------')
    print('Welcome: Tiger')
    print('-------------------------------')



@client.event
async def on_command_error(ctx , error):
        if isinstance(error , commands.CommandNotFound):
            await ctx.send ('Unrecognized Command')


@client.event
async def on_member_join(member):
    channel = client.get_channel(869982255622287361)
    membersplit = str(member)
    member_name , member_discriminator = membersplit.split('#')
    print(f'{member} has joined the server!')
    await channel.send(f'Welcome to S-VSMs Community Discord {member_name}! Please read the rules and react to continue!')



@client.event
async def on_member_remove(member):
    channel = client.get_channel(869760208656810035)
    membersplit = str(member)
    member_name , member_discriminator = membersplit.split('#')
    print(f'{member}has left the server!')
    await channel.send(f'{member_name} has left the server!')




@client.event
async def on_raw_reaction_add(payload , * role : discord.Role):
    if payload.message_id == 869988944752812132:
        role = (discord.utils.get(payload.member.guild.roles , name = 'Member'))
        await payload.member.add_roles(role)










@client.command(hidden = True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command(hidden = True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(self, ctx , * , member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name , member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
@unban.error
async def unban_error(self , ctx , error):
    if isinstance(error , commands.MissingPermissions):
        await ctx.send ('You do not have permission to do that')




@tasks.loop(minutes=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))






client.run(geese)
