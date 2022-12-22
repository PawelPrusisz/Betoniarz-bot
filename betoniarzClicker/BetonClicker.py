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


    @staticmethod
    async def hello():
        print("BetonClicker says")

    async def mine(self, interaction: discord.Interaction):
        mined_beton = randint(1,5)
        self.betonClickerDB.add_beton(interaction.user.id, mined_beton)
        await interaction.response.send_message(f"<@{interaction.user.id}> kopie b b b b beton!")
        await interaction.followup.send(f"<@{interaction.user.id}> wykopał {mined_beton} betonu!")
        
