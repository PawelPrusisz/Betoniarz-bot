from os.path import isfile
from sqlite3 import connect


DB_PATH ="./data/dbBetoniarzClicker/database.db"
BUILD_PATH="./data/dbBetoniarzClicker/build.sql"

cxn = connect(DB_PATH, check_same_thread=False)
cur = cxn.cursor()

class BetonClickerDB():

	@staticmethod
	def with_commit( func):
		def inner(*args, **kwargs):
			func(*args, **kwargs)
			cxn.commit()
		return inner

	@with_commit
	def build(self):
		if isfile(BUILD_PATH):
			self.scriptexec(BUILD_PATH)

	def get_cur(self):
		return cxn.cursor()

	def commit(self):
		cxn.commit()

	def close(self):
		cxn.close()

	def field(self, command, *values):
		cur.execute(command, tuple(values))

		if (fetch := cur.fetchone()) is not None:
			return fetch[0]


	def record(self, command, *values):
		cur.execute(command, tuple(values))
		return cur.fetchone()


	def records(self, command, *values):
		cur.execute(command, tuple(values))
		return cur.fetchall()


	def column(self, command, *values):
		cur.execute(command, tuple(values))
		return [item[0] for item in cur.fetchall()]


	def execute(self, command, *values):
		cur.execute(command, tuple(values))


	def multiexec(self, command, valueset):
		cur.executemany(command, valueset)


	def scriptexec(self, path):
		with open(path, "r", encoding="utf-8") as script:
			cur.executescript(script.read())

	def add_beton(self, user, beton_amount):
		print(f"Dodaje beton do użytkowina {user}")
		if cur.execute(f"SELECT UserID FROM users WHERE UserID = ?", (user,)).fetchone():
			print("add beton to existing user")
			self.execute(f"UPDATE users SET BetonAmount = BetonAmount + {beton_amount} WHERE UserID = {user}")
		else:
			print("create new user")
			self.execute(f"INSERT INTO users (UserID,  Level, Money, BetonAmount) VALUES (?, ?, ? ,?)", user, 0, 0, beton_amount)
		self.commit()