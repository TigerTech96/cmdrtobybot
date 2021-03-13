import discord
from discord import *
from discord.ext import commands
import wikipedia
import asyncio
import lxml


class Wiki(commands.Cog):


	def __init__(self, client):
		self.client = client
		print ('Loaded Wikipedia search')

	@commands.command(brief = 'Returns some wikipedia info on a subject' , description = 'Retunrs info from wikipedia from the typed subject i.e >wiki Dogs')
	#change comment
	async def wiki(self, ctx , message=None):
		str (message)
		suggestion1 = wikipedia.suggest(message)
		try:
			await ctx.send (wikipedia.summary(suggestion1))
		except wikipedia.exceptions.DisambiguationError as diswiki:
			wikioptions = diswiki.options
			await ctx.send ('Did you mean:' + wikioptions)
		
		


def setup(client):
	client.add_cog(Wiki(client))
