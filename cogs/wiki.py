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
		await ctx.send (wikipedia.summary(question))
		#await ctx.send ('Did you mean?' + wikipedia.suggest(question))
		#await asyncio.sleep(3)
		#if 
		
		


def setup(client):
	client.add_cog(Wiki(client))
