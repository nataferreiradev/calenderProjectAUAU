import sqlite3

class DataBase:
  def __init__(self):
    self.db = sqlite3.connect('calendar.db')
    
  def initCursor(self):
    return self.db.cursor()
  
  def closeCursor(self,cursor):
    self.db.commit()
    cursor.close()