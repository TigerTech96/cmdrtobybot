import discord
from discord import *
from discord.ext import commands
import os
class ChatBot(commands.Cog):


	def __init__(self, client):
		self.client = client
		print('Loaded Chatbbot....')
		
		
	@commands.command(brief = 'This is an experimental feature and should not be used' , description = 'Prompts the bot to start a chatbot session with you in a PM')
	async def letstalk(self , ctx):
		await ctx.author.send ('Okay let\'s get personal...')
		

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self:
			return
		

def setup(client):
	client.add_cog(ChatBot(client))
