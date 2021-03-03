import discord
from discord import *
from discord.ext import commands
import os
class Chatbot(commands.Cog):


	def __init__(self, client):
		self.client = client
		print('Loaded Chatbbot....')

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self:
			return
		if message.content == True:
			usermessage = message.content
			with open('chatlog.txt' , 'w') as f:
				f.write(message.author + ':' + usermessage)
				if message.content == 'Good Bot':
					await message.channel.send ('(ᵔᴥᵔ)')

def setup(client):
	client.add_cog(Chatbot(client))
