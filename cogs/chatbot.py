import discord
from discord import *
from discord.ext import commands

class Chatbot(commands.Cog):


	def __init__(self, client):
		self.client = client
		print('Loaded Chatbbot....')

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self:
			return
		if message.content == 'Good Bot':
			await message.channel.send ('(ᵔᴥᵔ)')
		if message.content == 'whoami':
			authorstring = str(message.author)
			await message.channel.send(authorstring)
		if message.content == 'secretsecret':
			await message.delete()
			await message.channel.send('────────█████─────────────█████')
			await message.channel.send('────████████████───────████████████')
			await message.channel.send('────████████████───────████████████')
			await message.channel.send('──████▓▓▓▓▓▓▓▓▓▓██───███▓▓▓▓▓▓▓▓▓████')
			await message.channel.send('─███▓▓▓▓▓▓▓▓▓▓▓▓▓██─██▓▓▓▓▓▓▓▓▓▓▓▓▓███')
			await message.channel.send('███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███')
			await message.channel.send('██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██')
			await message.channel.send('██▓▓▓▓▓▓▓▓▓──────────────────▓▓▓▓▓▓▓▓██')
			await message.channel.send('██▓▓▓▓▓▓▓─██───████─█──█─█████─▓▓▓▓▓▓██')
			await message.channel.send('██▓▓▓▓▓▓▓─██───█──█─█──█─██────▓▓▓▓▓▓██')
			await message.channel.send('███▓▓▓▓▓▓─██───█──█─█──█─█████─▓▓▓▓▓▓██')
			await message.channel.send('███▓▓▓▓▓▓─██───█──█─█──█─██────▓▓▓▓▓▓██')
			await message.channel.send('─███▓▓▓▓▓─████─████─████─█████─▓▓▓▓███')
			await message.channel.send('───███▓▓▓▓▓──────────────────▓▓▓▓▓▓███')
			await message.channel.send('────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████')
			await message.channel.send('─────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████')
			await message.channel.send('───────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████')
			await message.channel.send('──────────████▓▓▓▓▓▓▓▓▓▓▓▓████')
			await message.channel.send('─────────────███▓▓▓▓▓▓▓████')
			await message.channel.send('───────────────███▓▓▓███')
			await message.channel.send('─────────────────██▓██')
			await message.channel.send('──────────────────███')


def setup(client):
	client.add_cog(Chatbot(client))