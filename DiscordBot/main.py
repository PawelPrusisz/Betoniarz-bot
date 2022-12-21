import discord
import time
import re

class Betoniarz(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
        # Logs
        self.logsChannel:int = 1054732551945719889
        # Guilds
        self.kretoKraft: discord.Guild = None 
        # Users
        self.Seba:int = 697793376631914507
        self.Montysz:int = 287953869374226443
        self.Pawulenko:int = 221975880287780864
        self.Kreto:int = 287908668677160960
        self.Trela:int = 429304516601577472
        self.Hybrid:int = 289054007039754247
        # Channels
        self.DupaStrakaChannel:int = 1040722067353514034
        self.GeneralChannel:int = 1030776717666684990
        # Roles   
        self.Baba:discord.Role = None
        # Misc
        self.LastSeenBaba:int = 0
        # Token
        f = open("token.txt", 'r')
        self.DiscordToken = f.readline()

    async def on_message(self, message: discord.Message):
        if message.author != self.user:
            
            await self.userTagChecks(message)
            await self.roleCheck(message)
            await self.messageInBannedChannel(message)
            
            await printDebug(client=self, message=message)

    async def messageInBannedChannel(self, message: discord.Message):
        if message.channel.id == self.DupaStrakaChannel:
            await self.kretoKraft._channels[self.GeneralChannel].send(f'Użytkownik <@{message.author.id}> próbował wysłac wiadomość: \"{message.content}\" na kanale <#{self.DupaStrakaChannel}> @everyone')
            await message.delete()

    async def roleCheck(self, message):
        for role in message.author.roles:
            if self.Baba.id == role.id:
                now = time.time()
                if now - self.LastSeenBaba > 60:
                    self.LastSeenBaba = now
                    await printCommandDebug(self, f"BABA ALERT {message.author.display_name} BABA ALERT")
                    await message.channel.send(f'⚠️UWAGA⚠️ powyższa wiadomośc została wysłana przez k*biete i powinna zostac zignorowana')

    async def userTagChecks(self, message):
        if f'<@{self.Seba}>' in message.content:
            await printCommandDebug(self, f"⚠️BOOMER ALERT⚠️")
            await message.channel.send(f'⚠️BOOMER ALERT⚠️')
        elif f'<@{self.Hybrid}>' in message.content:
            await printCommandDebug(self, f"⚠️BABA ALERT⚠️")
            await message.channel.send(f'⚠️BABA ALERT⚠️')
        elif f'<@{self.Montysz}>' in message.content:
            await printCommandDebug(self, f"⚠️ANIME ALERT⚠️")
            await message.channel.send(f'⚠️ANIME ALERT⚠️')
        elif f'<@{self.Pawulenko}>' in message.content:
            await printCommandDebug(self, f"⚠️ESO ALERT⚠️")
            await message.channel.send(f'⚠️ESO ALERT⚠️')
        elif f'<@{self.Kreto}>' in message.content:
            await printCommandDebug(self, f"⚠️SCAM ALERT⚠️")
            await message.channel.send(f'⚠️SCAM ALERT⚠️')
        elif f'<@{self.Trela}>' in message.content:
            await printCommandDebug(self, f"Trela prosze powiedz kim jesteś")
            await message.channel.send(f'Trela prosze powiedz kim jesteś')

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=self.kretoKraft)
            await tree.sync(guild=discord.Object(1020307145213890571))
            self.synced = True
        print(f"Logged in as {self.user}")
        self.kretoKraft = self.get_guild(1030776717058519120)
        self.Baba = self.kretoKraft.get_role(1030785318540034058)

async def printDebug(client: Betoniarz, message: discord.Message):
    await client.get_channel(client.logsChannel).send(f"Got message: {message.content} from {message.author}")
    print(f"Got message: {message.content} from {message.author}")

async def printCommandDebug(client: Betoniarz, message: str):
    print(client)
    print(type(client))
    await client.get_channel(client.logsChannel).send(message)
    print(message)


betoniarz = Betoniarz()
tree = discord.app_commands.CommandTree(betoniarz)

@tree.command(name="beton", description='Betoniarze!', guild=betoniarz.kretoKraft)
async def self(interaction: discord.Interaction):
    await printCommandDebug(client=betoniarz, message=f"{interaction.user.name} używa /beton na serwerze {interaction.guild.name}")
    await interaction.response.send_message(f"<@{betoniarz.Seba}> https://www.youtube.com/watch?v=rc7k3G4LdN4")

@tree.command(name="beton", description='Betoniarze!', guild=discord.Object(1020307145213890571))
async def self(interaction: discord.Interaction):
    await printCommandDebug(client=betoniarz, message=f"{interaction.user.name} używa /beton na serwerze {interaction.guild.name}")
    await interaction.response.send_message(f"<@{betoniarz.Pawulenko}> https://www.youtube.com/watch?v=rc7k3G4LdN4")

@tree.command(name="clear", description='Clean all messages in the channel', guild=discord.Object(1020307145213890571))
async def self(interaction: discord.Interaction):
    currentChannel = betoniarz.get_channel(interaction.channel_id)
    result = await currentChannel.purge(check=lambda x: True)

    print(f"\n\n\n{result}")
    await printCommandDebug(client=betoniarz, message=f"Deleted all messages in \'{interaction.channel.name}\' channel on {interaction.guild.name} server")
    await interaction.response.pong()

betoniarz.run(betoniarz.DiscordToken)