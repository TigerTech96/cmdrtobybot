import discord
from discord import *
from discord.ext import commands
import os
class ChaTTBot(commands.Cog):


	def __init__(self, client):
		self.client = client
		print('Loaded Chatbbot....')

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self:
			return
		

def setup(client):
	client.add_cog(Chatbot(client))
