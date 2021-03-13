import discord
from discord import *
from discord.ext import commands
import wikipedia
import asyncio


class Wiki(commands.Cog):


	def __init__(self, client):
		self.client = client
		print ('Loaded Wikipedia search')

	@commands.command()
	async def wiki(self, ctx, *, question):
		str (question)
		try:
			await ctx.send (wikipedia.summary(question))
		except wikipedia.exceptions.DisambiguationError as diswiki:
			wikioptions = diswiki.options
			await ctx.send ('Did you mean:' + wikioptions)
		
		


def setup(client):
	client.add_cog(Wiki(client))
