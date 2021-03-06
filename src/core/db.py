import MySQLdb

class DB(object):
	"""
	Object encapsulating the database connection and operations.
	"""

	def __init__(self, dbName = "questionnaire"):
		self._dbName = dbName
		self._connect()

	def _connect(self):
		"""
		Connects to the MySQL database and creates a cursor.

		TODO: Should probably be using this within a with() to automatically
		close the cursor after use. Should also use connection pooling.
		"""
		self._db = MySQLdb.connect(
			host = "localhost",
			user = "root",
			passwd = "",
			db = self._dbName
		)
		self._dbHandle = self._db.cursor()

	def query(self, queryStr, *arguments):
		"""
		Executes the given query and returns the results.

		:param query: The SQL to execute.
		:param arguments: Arguments for the query.
		:return: :ist of column:value dictionaries.
		"""
		for query in queryStr.split(";"):
			self._dbHandle.execute(query, arguments)
		return self._dictFetchAll()

	def _dictFetchAll(self):
		"""
		Creates a dictionary of column:value from the results of a raw query.

		:return: Dictionary column:value.
		"""
		desc = self._dbHandle.description
		return [
			dict(zip([col[0] for col in desc], row))
			for row in self._dbHandle.fetchall()
		]

	def commit(self):
		"""
		Commits any changes.
		"""
		self._db.commit()

	def lastRowId(self):
		return self._dbHandle.lastrowid

	def close(self):
		"""
		Closes the handle and connection.
		"""
		self._dbHandle.close()
		self._db.close()

	def __str__(self):
		return "DB(db: %s, dbName: %s)" % (self._db, self._dbName)

	def __repr__(self):
		return "DB(%s, %s)" % (self._db, self._dbName)

dbInstance = DB()
