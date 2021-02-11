import discord
from discord.ext import commands
import discord.utils
import youtube_dl
import os
import asyncio

class Music(commands.Cog):


	def __init__(self, client):
		self.client = client
		print ('Loaded Music....')

	@commands.command()
	async def play(self, ctx , url : str):
		await ctx.message.delete()
		song_there = os.path.isfile('song.wav')
		try:
			if song_there:
				os.remove('song.wav')
		except PermissionError:
			await ctx.send('Wait for the current music to finish, or use the leave command')
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
			ydl.download([url])
		for file in os.listdir('./'):
			if file.endswith('.wav'):
				os.rename(file , 'song.wav')
		voice.play(discord.FFmpegPCMAudio('song.wav'))


	@commands.command()
	async def pause(self , ctx):
		await ctx.message.delete()
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)
		if voice.is_playing():
			await voice.pause()
		else:
			await ctx.send('No audio is currently playing')


	@commands.command()
	async def resume(self , ctx):
		await ctx.message.delete()
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)
		if voice.is_paused():
			await voice.resume()
		else:
			await ctx.send('No audio is currently paused')

	@commands.command()
	async def leave(self , ctx):
		await ctx.message.delete()
		voice = discord.utils.get(self.client.voice_clients , guild = ctx.guild)
		voice.stop()
		if voice.is_connected():
			await voice.disconnect()
		else:
			await ctx.send('I am not currently connected to a channel')


def setup(client):
	client.add_cog(Music(client))