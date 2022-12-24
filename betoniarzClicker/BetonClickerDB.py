from os.path import isfile
from sqlite3 import connect
import discord

DB_PATH = "./data/dbBetoniarzClicker/database.db"
BUILD_PATH = "./data/dbBetoniarzClicker/build.sql"

cxn = connect(DB_PATH, check_same_thread=False)
cur = cxn.cursor()


class BetonClickerDB:
    @staticmethod
    def with_commit(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            cxn.commit()

        return inner

    @with_commit
    def build(self):
        if isfile(BUILD_PATH):
            self.script_exec(BUILD_PATH)

    @staticmethod
    def script_exec(path):
        with open(path, "r", encoding="utf-8") as script:
            cur.executescript(script.read())

    def add_beton(self, user_id, beton_amount):
        if cur.execute(f"SELECT UserID FROM users WHERE UserID = ?", (user_id,)).fetchone():
            cur.execute(f"UPDATE users SET BetonAmount = BetonAmount + {beton_amount} "
                        f"WHERE UserID = {user_id}")
        else:
            self.add_new_user(user_id, beton_amount=beton_amount)
        cxn.commit()

    async def show_beton(self, interaction: discord.Interaction):
        stats = self.load_stats(interaction.user.id)
        if not stats:
            self.add_new_user(interaction.user.id)
            stats = self.load_stats(interaction.user.id)
            cxn.commit()

        embed = discord.Embed(title=f"Statystyki betoniarza {interaction.user.name}",
                              description=f"Poziom: {stats[0]}\n"
                                          f"Kasa: {stats[1]}$\n"
                                          f"Beton: {stats[2]}",
                              color=0x00ff00)
        embed.set_thumbnail(url=interaction.user.avatar.url)
        return embed

    @staticmethod
    def add_new_user(user_id, level=0, money=0, beton_amount=0):
        print("create new user: ", user_id, level, money, beton_amount)
        return cur.execute(
            f"INSERT INTO users (UserID, Level, Money, BetonAmount) "
            f"VALUES (?, ?, ?, ?)", (user_id, level, money, beton_amount))

    @staticmethod
    def load_stats(user_id: int):
        return cur.execute(f"SELECT Level, Money, BetonAmount FROM users WHERE UserID = ?", (user_id,)).fetchone()
