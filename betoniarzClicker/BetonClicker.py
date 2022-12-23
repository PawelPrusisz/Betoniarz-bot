import discord
from Betoniarz import Betoniarz
from random import randint
import asyncio
from discord.ext import commands
from betoniarzClicker.BetonClickerDB import *


class BetonClicker():

    def __init__(self, betoniarz: Betoniarz):
        self.betoniarz = betoniarz
        tree = betoniarz.tree 
        self.betonClickerDB = BetonClickerDB()

    async def mine(self, interaction: discord.Interaction):
        mined_beton = randint(1,5)
        self.betonClickerDB.add_beton(interaction.user.id, mined_beton)
        await interaction.response.send_message(f"<@{interaction.user.id}> kopie b b b b beton!")
        await interaction.followup.send(f"<@{interaction.user.id}> wykopał {mined_beton} betonu!")
    async def show_beton(self, interaction: discord.Interaction):
        if not (self.betonClickerDB.record(f"SELECT * FROM users WHERE UserID = ?", interaction.user.id)):
            self.betonClickerDB.execute(f"INSERT INTO users (UserID, Level, Money, Beton) VALUES (?, ?, ?, ?)", interaction.user.id, 0, 0, 0)
        data = self.betonClickerDB.record(f"SELECT * FROM users WHERE UserID = ?", interaction.user.id)
        level = data[1]
        money = data[2]
        beton = data[3]
        embed = discord.Embed(title=f"Statystyki betoniarza {interaction.user.name}", description=f"Poziom: {level}\nKasa: {money}$\nBeton: {beton}", color=0x00ff00)
        embed.set_thumbnail(url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed)
        
