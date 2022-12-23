from KretoKraftClient import KretoKraftClient
import discord
import time
import anime_images_api
import random
from discord_data_constans.users import *
from discord_data_constans.channels import *


class Betoniarz(KretoKraftClient):
    def __init__(self):
        KretoKraftClient.__init__(self)
        self.synced = False

        # API
        self.AnimeAPI: anime_images_api.Anime_Images = anime_images_api.Anime_Images()

        # Misc
        self.LastSeenBaba: int = 0
        self.UserTagCooldown: int = 0
        self.animeOpions = ['hug', 'kiss', 'cuddle', 'pat', 'wink']
        self.animeOpionsNSFW = ['boobs', 'hentai']

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync(guild=self.kretoKraft)
            await self.tree.sync(guild=discord.Object(1020307145213890571))
            self.synced = True
        print(f"Logged in as {self.user}")
        self.kretoKraft = self.get_guild(1030776717058519120)
        self.Baba = self.kretoKraft.get_role(1030785318540034058)
        self.Anime = self.kretoKraft.get_role(1033361271069868032)

    async def on_message(self, message: discord.Message):
        if message.author.id != BETONIARZ:
            await self.user_tag_checks(message)
            await self.role_check(message)
            await self.message_in_banned_channel(message)
            await self.print_debug(message=message)

    async def message_in_banned_channel(self, message: discord.Message):
        if message.channel.id == DUPA_SRAKA_CHANNEL:
            await self.kretoKraft.channels[GENERAL_CHANNEL].send(
                f'Użytkownik <@{message.author.id}> próbował wysłac wiadomość: \"{message.content}\" na kanale <#{DUPA_SRAKA_CHANNEL}> @everyone')
            await message.delete()

    async def role_check(self, message: discord.Message):
        for role in message.author.roles:
            if 1030785318540034058 == role.id:
                now = time.time()
                if now - self.LastSeenBaba > 60:
                    self.LastSeenBaba = now
                    await self.printCommandDebug(f"BABA ALERT {message.author.display_name} BABA ALERT")
                    await message.channel.send(
                        f'⚠️UWAGA⚠️ powyższa wiadomośc została wysłana przez k*biete i powinna zostac zignorowana')

    async def user_tag_checks(self, message: discord.Message):
        now = time.time()
        if now - self.UserTagCooldown > 5:
            print(f"anime: {self.Anime.id}")
            if f'<@{SEBA}>' in message.content:
                await self.handle_message(message, '⚠️BOOMER ALERT⚠️')
            elif f'<@{HYBRID}>' in message.content:
                await self.handle_message(message, '⚠️BABA ALERT⚠️')
            elif f'<@{MONTYSZ}>' in message.content:
                await self.handle_message(message, '⚠️ANIME ALERT⚠️')
            elif f'<@{PAWULENKO}>' in message.content:
                await self.handle_message(message, '⚠️ESO ALERT⚠️')
            elif f'<@{KRETO}>' in message.content:
                await self.handle_message(message, '⚠️SCAM ALERT⚠️')
            elif f'<@{TRELA}>' in message.content:
                await self.handle_message(message, 'Trela prosze powiedz kim jesteś')
            elif f'<@{BETONIARZ}>' in message.content:
                await self.handle_message(message, f'<@{message.author.id}> ty jebany betoniarzu')
            elif f'<@&{self.Anime.id}>' in message.content:
                await self.hande_anime_message(message)
            else:
                return
            self.UserTagCooldown = now

    async def hande_anime_message(self, message: discord.Message):
        nsfw = 'nsfw' in message.content.lower()
        if nsfw:
            anime_girl = self.AnimeAPI.get_nsfw(random.choice(self.animeOpionsNSFW))
            nsfw = True
        else:
            anime_girl = self.AnimeAPI.get_sfw(random.choice(self.animeOpions))
        embed = discord.Embed()
        embed.set_image(url=anime_girl)
        await self.print_command_debug(f'Łap anime dzieczynke zboczeńcu <@{message.author.id}>')
        if nsfw:
            await message.channel.send(content=f'Łap anime dzieczynke zboczeńcu <@{message.author.id}>', embed=embed,
                                       delete_after=3.0)
        else:
            await message.channel.send(content=f'Łap anime dzieczynke zboczeńcu <@{message.author.id}>', embed=embed)
