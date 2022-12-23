from random import randint

from Betoniarz import Betoniarz
from betoniarzClicker.BetonClickerDB import *


class BetonClicker:

    def __init__(self, betoniarz: Betoniarz):
        self.betoniarz = betoniarz
        self.betonClickerDB = BetonClickerDB()

    async def mine(self, interaction: discord.Interaction):
        mined_beton = randint(1, 695)

        self.betonClickerDB.add_beton(interaction.user.id, mined_beton)
        await interaction.response.send_message(f"<@{interaction.user.id}> kopie b b b b beton!")
        await interaction.followup.send(f"<@{interaction.user.id}> wykopał {mined_beton} betonu!")

    async def show_beton(self, interaction: discord.Interaction):
        embed = await self.betonClickerDB.show_beton(interaction)
        await interaction.response.send_message(embed=embed)
