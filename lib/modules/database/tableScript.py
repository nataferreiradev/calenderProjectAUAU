from ..controllers.userController import UserController
from ..controllers.checkListDayController import CheckListDayController
from ..controllers.checkListNotationController import CheckListNotationController
from ..controllers.NotationController import NotationController
from ..controllers.categoryController import CategoryController


class TableScript:
  tables = {
    UserController.TABLENAME:
    f"""create table if not exists {UserController.TABLENAME}(
        {UserController.ID_USER}  integer primary key AUTOINCREMENT,
        {UserController.EMAIL}    varchar(100),
        {UserController.USER}     varchar(100),
        {UserController.PASSWORD} varchar(200),
        {UserController.STATS}    char(2)
    );""",
    CheckListDayController.TABLENAME:
    f"""create table if not exists {CheckListDayController.TABLENAME}(
        {CheckListDayController.IDCHECKLISTDAY} integer primary key AUTOINCREMENT,
        {CheckListDayController.ID_USER}        integer,
        {CheckListDayController.ORDER}          integer,
        {CheckListDayController.DAY}            date,
        {CheckListDayController.STATS}          char(2),
  
        FOREIGN KEY ({CheckListDayController.ID_USER}) REFERENCES {UserController.TABLENAME}({UserController.ID_USER})                                   
    );""",
    CheckListNotationController.TABLENAME:
    f"""create table if not exists {CheckListNotationController.TABLENAME}(
        {CheckListNotationController.IDCHECKLISTNOTATION} integer primary key AUTOINCREMENT,
        {CheckListNotationController.CONTENT}             varchar(200),
        {CheckListNotationController.STATS}               char(2),
        {CheckListNotationController.IDNOTATION}          integer,
        {CheckListNotationController.ORDER}               integer
    );""",
    NotationController.TABLENAME:
    f"""create table if not exists {NotationController.TABLENAME}(
        {NotationController.ID_NOTATION} integer primary key AUTOINCREMENT,
        {NotationController.ID_USER}     integer,
        {NotationController.DATE}        date,
        {NotationController.TITLE}       varchar(100),
        {NotationController.COMMENT}     varchar(500),
        {NotationController.TIMEINIT}    date,
        {NotationController.TIMEEND}     date,
        {NotationController.FEEDBACK}    int(1),
        {NotationController.IDCATEGORY}  int,
        {NotationController.STATS}       char(2),
  
        FOREIGN KEY ({NotationController.ID_USER}) REFERENCES {UserController.TABLENAME}({UserController.ID_USER}),
        FOREIGN KEY ({NotationController.ID_NOTATION}) REFERENCES {CategoryController.TABLENAME}({CategoryController.IDCATEGORY})
    );""",
    CategoryController.TABLENAME:
    f"""create table if not exists {CategoryController.TABLENAME}(
        {CategoryController.IDCATEGORY}  integer primary key AUTOINCREMENT,
        {CategoryController.DESCRIPTION} varchar(300),s
        {CategoryController.COLOR}       integer,
        {CategoryController.STATS}       char(2),
        {CategoryController.IDUSER}      integer,
        
        FOREIGN KEY ({CategoryController.IDUSER}) REFERENCES {UserController.TABLENAME}({UserController.ID_USER})
    );""",
  }
  