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
		song_there = os.path.isfile('song.wav')
		try:
			if song_there:
				os.remove('song.wav')
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
				os.rename(file , 'song.wav')
		voice.play(discord.FFmpegPCMAudio('song.wav'))



	@commands.command()
	async def WHAT(self, ctx):
		await ctx.message.delete()
		song_there = os.path.isfile('song.wav')
		try:
			if song_there:
				os.remove('song.wav')
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
				os.rename(file , 'song.wav')
		voice.play(discord.FFmpegPCMAudio('song.wav'))




	@commands.command()
	async def FIREFIGHT(self, ctx):
		await ctx.message.delete()
		song_there = os.path.isfile('song.wav')
		try:
			if song_there:
				os.remove('song.wav')
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
				os.rename(file , 'song.wav')
		voice.play(discord.FFmpegPCMAudio('song.wav'))
		while voice.is_playing():
			sleep(1)
		voice.stop()
		await voice.disconnect()





	@commands.command()
	async def HELL(self, ctx):
		await ctx.message.delete()
		song_there = os.path.isfile('song.wav')
		try:
			if song_there:
				os.remove('song.wav')
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
				os.rename(file , 'song.wav')
		voice.play(discord.FFmpegPCMAudio('song.wav'))


def setup(client):
	client.add_cog(Memes(client))