from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# Global Variables
SQLITE                  = 'sqlite'


# Table Names
USERS           = 'users'
ADDRESSES       = 'addresses'

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
        self.session = None
        
        if self.dbtype in self.DB_ENGINE.keys():
            self.engine_url = self.DB_ENGINE[self.dbtype].format(DB=dbname)
            self.db_engine = create_engine(self.engine_url, echo = True)
            print("engine setup", self.db_engine)
            
        else:
            print("DBType is not found in DB_ENGINE")
            
    def session_manager(self):
        try:
            Session = sessionmaker()
            Session.configure(bind=self.db_engine)
        except Exception as ae:
            print(ae)
        self.session = Session()
        return self.session
            
    
    # def create_db_tables(self):
    #     metadata = MetaData()
    #     users = Table(USERS, metadata,
    #                 Column('id', Integer, primary_key=True),
    #                 Column('first_name', String),
    #                 Column('last_name', String)
    #                 )

    #     address = Table(ADDRESSES, metadata,
    #                     Column('id', Integer, primary_key=True),
    #                     Column('user_id', None, ForeignKey('users.id')),
    #                     Column('email', String, nullable=False),
    #                     Column('address', String)
    #                     )

    #     try:
    #         ## This will create the tables struct
    #         metadata.create_all(self.db_engine)
    #         print("Tables created")
    #     except Exception as e:
    #         print("Error occurred during Table creation!")
    #         print(e)
            
    # def execute_query(self, query=''):
    #     if query == '' : return

    #     print (query)
    #     with self.db_engine.connect() as connection:
    #         try:
    #             connection.execute(query)
    #         except Exception as e:
    #             print(e)


    # def print_all_data(self, table='', query=''):
    #     query = query if query != '' else "SELECT * FROM '{}';".format(table)
    #     print(query)

    #     with self.db_engine.connect() as connection:
    #         try:
    #             result = connection.execute(query)
    #         except Exception as e:
    #             print(e)
    #         else:
    #             for row in result:
    #                 print(row) # print(row[0], row[1], row[2])
    #             result.close()

    #     print("\n")

    # # Examples

    # def sample_query(self):
    #     # Sample Query
    #     query = "SELECT first_name, last_name FROM {TBL_USR} WHERE " \
    #             "last_name LIKE 'M%';".format(TBL_USR=USERS)
    #     self.print_all_data(query=query)

    #     # Sample Query Joining
    #     query = "SELECT u.last_name as last_name, " \
    #             "a.email as email, a.address as address " \
    #             "FROM {TBL_USR} AS u " \
    #             "LEFT JOIN {TBL_ADDR} as a " \
    #             "WHERE u.id=a.user_id AND u.last_name LIKE 'M%';" \
    #         .format(TBL_USR=USERS, TBL_ADDR=ADDRESSES)
    #     self.print_all_data(query=query)

    # def sample_delete(self):
    #     # Delete Data by Id
    #     query = "DELETE FROM {} WHERE id=3".format(USERS)
    #     self.execute_query(query)
    #     self.print_all_data(USERS)

    #     # Delete All Data
    #     '''
    #     query = "DELETE FROM {}".format(USERS)
    #     self.execute_query(query)
    #     self.print_all_data(USERS)
    #     '''

    # def sample_insert(self):
    #     # Insert Data
    #     query = "INSERT INTO {}(id, first_name, last_name) " \
    #             "VALUES (3, 'Terrence','Jordan');".format(USERS)
    #     self.execute_query(query)
    #     self.print_all_data(USERS)

    # def sample_update(self):
    #     # Update Data
    #     query = "UPDATE {} set first_name='XXXX' WHERE id={id}"\
    #         .format(USERS, id=3)
    #     self.execute_query(query)
    #     self.print_all_data(USERS)

