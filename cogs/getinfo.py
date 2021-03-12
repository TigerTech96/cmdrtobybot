import discord
from discord import *
from discord.ext import commands
import discord.utils

class Getinfo(commands.Cog):


	def __init__(self, client):
		self.client = client
		print ('Loaded Getinfo....')

	@commands.command(brief = 'Gives the ID of the specified channel')
	async def getchannel(self , ctx, *, given_name=None):
		for channel in ctx.guild.channels:
			if channel.name == given_name:
				wanted_channel_id = channel.id

		await ctx.send(wanted_channel_id) # this is just to check


def setup(client):
	client.add_cog(Getinfo(client))
