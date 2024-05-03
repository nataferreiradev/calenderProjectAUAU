from ..models.user import user
from ..database.immediate import Immediate

class UserController:
  TABLENAME = 'user'
  ID_USER = "id_user"
  EMAIL = "email"
  USER = "user"
  PASSWORD = "password" 
  STATS = "stats"
  
  def insertUser(user: user):
    sql = f"""insert into {UserController.TABLENAME} 
              ({UserController.EMAIL,UserController.USER,UserController.PASSWORD,UserController.STATS})
              value ('{user.email}','{user.user}','{user.password}','{user.stats}');
          """;
    resp = Immediate.execute(sql);
    if resp:
      print(resp)