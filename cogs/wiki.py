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

	@commands.command(brief = 'Returns some wikipedia info on a subject' , description = 'Returns info from wikipedia from the typed subject i.e >wiki Dogs')
	#change comment
	async def wiki(self, ctx , message=None):
		str (message)
		print (message)
		try:
			print ('trying to type summary')
			print (wikipedia.summary(message))
		except wikipedia.exceptions.DisambiguationError as e:
			print ('Attempting disambiguation')
			wikioptions = e.options
			wikioption = str (wikioptions)
			await ctx.send ('Did you mean:' + wikioptions)
		
		


def setup(client):
	client.add_cog(Wiki(client))
