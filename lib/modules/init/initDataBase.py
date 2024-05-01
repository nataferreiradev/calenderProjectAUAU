from modules.database.immediate import Immediate
from ..database.tableScript import TableScript

class initDataBase():
  def __init__(self):
    immediate = Immediate()
    for table in TableScript.tables:
      resp = immediate.execute(TableScript.tables[table])
      if resp:
        print(resp)
    resp = immediate.execute("select date('now') date")
    if resp:
      print("data base {} initialized".format(resp))
    else:
      print("error while try init dataBase")