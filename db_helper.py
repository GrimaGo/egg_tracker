import sqlite3

class DB:
	def __init__(self, db_file):
		self.conn = sqlite3.connect(db_file)

	def add_egg(self, trainer, dist, pokemon):
		c = self.conn.cursor()
		print("new egg:", trainer["id"], dist + "km", pokemon)
		c.execute("INSERT OR IGNORE INTO trainers(t_id, t_username) VALUES(?, ?)", (trainer["id"], trainer["username"]))
		c.execute("INSERT INTO eggs(trainer_id, distance, pokemon) VALUES(?, ?, ?)", (trainer["id"], dist, pokemon))
		self.conn.commit()