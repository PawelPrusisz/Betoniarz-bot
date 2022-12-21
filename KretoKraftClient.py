import discord

class KretoKraftClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.logsChannel:int = 1054732551945719889

        # Guilds
        self.kretoKraft: discord.Guild = None 

        # Roles   
        self.Anime:discord.Role = None
        self.Baba:discord.Role = None

        # Token
        f = open("token.token", 'r')
        self.DiscordToken = f.readline()
        self.tree = discord.app_commands.CommandTree(self)


    async def printDebug(self, message: discord.Message):
        await self.get_channel(self.logsChannel).send(f"Got message: {message.content} from {message.author}")
        print(f"Got message: {message.content} from {message.author}")

    async def printCommandDebug(self, message: str):
        print(self)
        print(type(self))
        await self.get_channel(self.logsChannel).send(message)
        print(message)

    async def handle_message(self, message: discord.Message, text: str):
        await self.printCommandDebug(f'<@{message.author.id}> {text}')
        await message.channel.send(f'<@{message.author.id}>  {text}')