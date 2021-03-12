import discord
from discord import *
from discord.ext import commands

class Usermanagement(commands.Cog):


	def __init__(self, client):
		self.client = client
		print ('Loaded User Management....')

	@commands.command(brief = 'Quick command to have bot kick specified user' , description = '>kick <user> , no identifier is needed unless multiple users share that account name')
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member : discord.Member, reason=None):
		await member.kick(reason=reason)
		kickmemberstr = str(member)
		print ('Kicked: ' + kickmemberstr)
	@kick.error
	async def kick_error(self , ctx , error):
		if isinstance(error , commands.MissingPermissions):
			await ctx.send ('You do not have permission to do that')


	@commands.command(brief = 'Quick command to have bot ban specified user' , description = '>ban <user> , no identifier is needed unless multiple users share that account name')
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member : discord.Member, reason=None):
		await member.ban(reason=reason)
		banmemberstr = str(member)
		await ctx.send(f'Banned {member.mention}')
		print ('Banned: ' + banmemberstr)
	@ban.error
	async def ban_error(self , ctx , error):
		if isinstance(error , commands.MissingPermissions):
			await ctx.send ('You do not have permission to do that')





def setup(client):
	client.add_cog(Usermanagement(client))
