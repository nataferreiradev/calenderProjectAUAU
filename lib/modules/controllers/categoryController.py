from ..models.category import category
from ..database.immediate import Immediate

class CategoryController:
  TABLENAME = 'category'
  IDCATEGORY = 'id_category'
  DESCRIPTION = 'description'
  COLOR = 'color'
  STATS = 'stats'
  IDUSER = 'id_user'
  
  def insertCategory(category: category):
    sql = f"""insert into {CategoryController.TABLENAME}({CategoryController.DESCRIPTION},{CategoryController.COLOR},{CategoryController.STATS},{CategoryController.IDUSER})
              values('{category.description}',{category.COLOR},'{category.stats}',{category.idUser});
          """
          
    resp = Immediate.execute(sql)
    if resp:
      print(resp)