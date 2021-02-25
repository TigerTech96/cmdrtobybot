import discord
from discord.ext import commands
import discord.utils
import youtube_dl
import os
import asyncio
import time

class Memes(commands.Cog):


	def __init__(self, client):
		self.client = client
		print ('Loaded Memes')

	@commands.command()
	async def STOP(self, ctx):
		await ctx.message.delete()
		song_there = os.path.isfile('law.wav')
		try:
			if song_there:
				os.remove('law.wav')
		except PermissionError:
			await ctx.send('Error')
			return
		voiceChannel = ctx.message.author.voice.channel
		await voiceChannel.connect()
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)

		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'wav',
				'preferredquality': '320',
			}],
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download(['https://www.youtube.com/watch?v=O2otihe65SI'])
		for file in os.listdir('./'):
			if file.endswith('.wav'):
				os.rename(file , 'law.wav')
		voice.play(discord.FFmpegPCMAudio('law.wav'))
		sleep (10)
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)
		while voice.is_playing(): #Checks if voice is playing
			await asyncio.sleep(1) #While it's playing it sleeps for 1 second
		else:
			await asyncio.sleep(15) #If it's not playing it waits 15 seconds
			while voice.is_playing(): #and checks once again if the bot is not playing
				break #if it's playing it breaks
			else:
				await voice.disconnect() #if not it disconnects
	@commands.command()
	async def WHAT(self, ctx):
		await ctx.message.delete()
		song_there = os.path.isfile('WHAT.wav')
		try:
			if song_there:
				os.remove('WHAT.wav')
		except PermissionError:
			await ctx.send('Error')
			return
		voiceChannel = ctx.message.author.voice.channel
		await voiceChannel.connect()
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)

		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'wav',
				'preferredquality': '320',
			}],
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download(['https://www.youtube.com/watch?v=W1yM0wVnpFU'])
		for file in os.listdir('./'):
			if file.endswith('.wav'):
				os.rename(file , 'WHAT.wav')
		voice.play(discord.FFmpegPCMAudio('WHAT.wav'))
		sleep (10)
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)
		while voice.is_playing(): #Checks if voice is playing
			await asyncio.sleep(1) #While it's playing it sleeps for 1 second
		else:
			await asyncio.sleep(15) #If it's not playing it waits 15 seconds
			while voice.is_playing(): #and checks once again if the bot is not playing
				break #if it's playing it breaks
			else:
				await voice.disconnect() #if not it disconnects

	@commands.command()
	async def FIREFIGHT(self, ctx):
		await ctx.message.delete()
		song_there = os.path.isfile('FIREFIGHT.wav')
		try:
			if song_there:
				os.remove('FIREFIGHT.wav')
		except PermissionError:
			await ctx.send('Error')
			return
		voiceChannel = ctx.message.author.voice.channel
		await voiceChannel.connect()
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)

		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'wav',
				'preferredquality': '320',
			}],
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download(['https://www.youtube.com/watch?v=wcKTbFbwrxE'])
		for file in os.listdir('./'):
			if file.endswith('.wav'):
				os.rename(file , 'FIREFIGHT.wav')
		voice.play(discord.FFmpegPCMAudio('FIREFIGHT.wav'))
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)
		while voice.is_playing():
			await sleep (1)
		await voice.disconnect


	@commands.command()
	async def HELL(self, ctx):
		await ctx.message.delete()
		song_there = os.path.isfile('HELL.wav')
		try:
			if song_there:
				os.remove('HELL.wav')
		except PermissionError:
			await ctx.send('Error')
			return
		voiceChannel = ctx.message.author.voice.channel
		await voiceChannel.connect()
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)

		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'wav',
				'preferredquality': '320',
			}],
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download(['https://www.youtube.com/watch?v=b29IKW3YrLA'])
		for file in os.listdir('./'):
			if file.endswith('.wav'):
				os.rename(file , 'HELL.wav')
		voice.play(discord.FFmpegPCMAudio('HELL.wav'))
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)
		while voice.is_playing():
			await sleep (1)
		await voice.disconnect



def setup(client):
	client.add_cog(Memes(client))