import sqlite3

from sqlalchemy import create_engine

# Global Variables
SQLITE                  = 'sqlite'

class Database:
    
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}',
    }
    
    db_engine = None
    
    def __init__(self,
                dbtype:str,
                username:str='',
                password:str='',
                dbname:str='') -> None:
        
        self.dbtype = dbtype.lower()
        self.engine_url = ""
        
        if self.dbtype in self.DB_ENGINE.keys():
            self.engine_url = self.DB_ENGINE[self.dbtype].format(DB=dbname)
            self.db_engine = create_engine(self.engine_url)
            print("engine setup", self.db_engine)
            
        else:
            print("DBType is not found in DB_ENGINE")
            



def connection():
    dbms = Database(SQLITE, dbname='travel.db')
    engine = dbms.db_engine
    return engine.connect()

        