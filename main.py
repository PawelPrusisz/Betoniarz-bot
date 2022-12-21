import discord
import time
import re
import anime_images_api
import random
from discord_data_constans.users import *
from Betoniarz import Betoniarz



betoniarz = Betoniarz()
tree = betoniarz.tree 

@tree.command(name="beton", description='Betoniarze!', guild=betoniarz.kretoKraft)
async def self(interaction: discord.Interaction):
    await betoniarz.printCommandDebug(message=f"{interaction.user.name} używa /beton na serwerze {interaction.guild.name}")
    await interaction.response.send_message(f"<@{SEBA}> https://www.youtube.com/watch?v=rc7k3G4LdN4")

@tree.command(name="beton", description='Betoniarze!', guild=discord.Object(1020307145213890571))
async def self(interaction: discord.Interaction):
    await betoniarz.printCommandDebug(message=f"{interaction.user.name} używa /beton na serwerze {interaction.guild.name}")
    await interaction.response.send_message(f"<@{PAWULENKO}> https://www.youtube.com/watch?v=rc7k3G4LdN4")

@tree.command(name="clear", description='Clean all messages in the channel', guild=discord.Object(1020307145213890571))
async def self(interaction: discord.Interaction):
    currentChannel = betoniarz.get_channel(interaction.channel_id)
    result = await currentChannel.purge(check=lambda x: True)

    print(f"\n\n\n{result}")
    await betoniarz.printCommandDebug(betoniarz, message=f"Deleted all messages in \'{interaction.channel.name}\' channel on {interaction.guild.name} server")
    await interaction.response.pong()


    

betoniarz.run(betoniarz.DiscordToken)