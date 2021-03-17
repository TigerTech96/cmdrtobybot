import discord
from discord import *
from discord.ext import commands
import wikipedia
import asyncio


class Wiki(commands.Cog):


	def __init__(self, client):
		self.client = client
		print ('Loaded Wikipedia search')

	@commands.command(brief = 'Returns some wikipedia info on a subject' , description = 'Returns info from wikipedia from the typed subject i.e >wiki Dogs')
	#change comment
	async def wiki(self, ctx , message=None):
		str (message)
		await ctx.send (wikipedia.summary(message), sentences = 1)
		
		


def setup(client):
	client.add_cog(Wiki(client))
