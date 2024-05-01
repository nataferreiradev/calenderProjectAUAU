from .database import DataBase 

class Immediate:
  def __init__(self):
    self._db = DataBase()
  
  def executeMany(self, sql, data: list):
    cursor = self._db.initCursor()
    resp = cursor.executemany(sql, data)
    results = resp.fetchall()
    self._db.closeCursor(cursor)
    return results

  def execute(self, sql):
    cursor = self._db.initCursor()
    resp = cursor.execute(sql)
    result = resp.fetchall()
    self._db.closeCursor(cursor)
    return result