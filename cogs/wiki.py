import discord
from discord import *
from discord.ext import commands
import wikipedia
import wikia

class Wiki(commands.Cog):


	def __init__(self, client):
		self.client = client
		print ('Loaded Wikipedia search')

	#@commands.command()
	#async def wiki(self, ctx, *, question):
		#str (question)
		#await ctx.send (wikipedia.summary(question))

	@commands.command()
	async def wiki(self, ctx, * , question):
		str (question)
		subject = wiki.page('Elite Dangerous' , question)
		print (wikia.summary)
		await ctx.send (wikia.summary)

def setup(client):
	client.add_cog(Wiki(client))