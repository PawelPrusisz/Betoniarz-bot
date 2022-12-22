import discord
import time
import re
import anime_images_api
import random
from discord_data_constans.users import *
from Betoniarz import Betoniarz
from betoniarzClicker.BetonClicker import BetonClicker
from datetime import timedelta
import sqlite3
from betoniarzClicker.BetonClickerDB import *
betoniarz = Betoniarz()
betoniarz_clicker = BetonClicker(betoniarz)
betonClickerDB = BetonClickerDB()
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
    await interaction.response.send_message(f"Done", delete_after=10.0)
    result = await currentChannel.purge(check=lambda x: True)
    print(f"\n\n\n{result}")
    await betoniarz.printCommandDebug(f"Deleted all messages in \'{interaction.channel.name}\' channel on {interaction.guild.name} server")

@tree.command(name="mine", description='mine', guild=betoniarz.kretoKraft)
@discord.app_commands.checks.cooldown(1,3)
async def self(interaction: discord.Interaction):
    await betoniarz.printCommandDebug(message=f"{interaction.user.name} używa /mine na serwerze {interaction.guild.name}")
    await betoniarz_clicker.mine(interaction)


@self.error
async def mineError(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    if isinstance(error, discord.app_commands.CommandOnCooldown):
        time_remaining = str(timedelta(seconds = int(error.retry_after)))
        await interaction.response.send_message(f"CZEKAJ KURWA jeszcze {time_remaining} sekund", ephemeral = True)



betonClickerDB.build()
betoniarz.run(betoniarz.DiscordToken)