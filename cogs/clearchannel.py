import discord
from discord import *
from discord.ext import commands

class ChannelControls(commands.Cog):


	def __init__(self, client):
		self.client = client
		print('Loaded Channel Controls....')

	@commands.command(brief = 'Clears messages in a channel' , description = 'Clears specified amount of messages from a channel, also deletes the command message used to call it, so no need to count the command message when specifying a number')
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount : int):
		await ctx.message.delete()
		await ctx.channel.purge(limit=amount)
	@clear.error
	async def clear_error(self , ctx , error):
		if isinstance(error , commands.MissingRequiredArgument):
			await ctx.send ('Please specify how many messages you would like to clear')
		if isinstance(error , commands.MissingPermissions):
			await ctx.send ('You do not have permission to do that')

		


def setup(client):
	client.add_cog(ChannelControls(client))
