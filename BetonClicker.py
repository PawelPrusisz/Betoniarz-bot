import discord
from Betoniarz import Betoniarz
from random import randint
import asyncio
from discord.ext import commands

class BetonClicker():


    def __init__(self, betoniarz: Betoniarz):
        self.betoniarz = betoniarz
        tree = betoniarz.tree 

    @staticmethod
    async def hello():
        print("BetonClicker says")

    @staticmethod
    async def mine(interaction: discord.Interaction):
        mine_time = randint(1,5)
        await interaction.response.send_message(f"<@{interaction.user.id}> kopie b b b b beton!")
        
        #await asyncio.sleep({mine_time})
        await interaction.followup.send(f"<@{interaction.user.id}> wykopał {randint(1,5)} betonu!")
