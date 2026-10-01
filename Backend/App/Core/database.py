from sqlalchemy import create_engine,text #Importing The Two Functions From The SQLAlchemy create_engine For Connection To The Database And text For Executing Raw SQL Queries.
from sqlalchemy.orm import sessionmaker,DeclarativeBase #The Sessionamker Fucntoion Is Used To Create A Session Object Which Will Be Used To Interact With The Database.

from App.Core.config import settings #Importing The Settings Object From The Config Module.

engine = create_engine(settings.database_url) #Creating The Engine Object Which Will Be Used To Connect To The Database Using The Configurable Value From The .env File.

SessionLocal = sessionmaker( #Creates A Session Factory Which Will Be Used To Create Session Objects For DB Interaction.
    bind=engine, 
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase): #Creating A Base Class Which Will Be Used To Define The Database Models.
    pass

def get_db(): #Function To Get A Database Session Which Will Be Used To Interact With The Database.
    db = SessionLocal() #Creating A Session Object Using The Session Factory.
    try:
        yield db #Yielding The Session Object To Be Used In The Dependency Injection.
    finally:
        db.close() #Closing The Session Object After The Request Is Completed.

def test_database_connection(): #Function To Test The Database Connection By Executing A Simple Query.
    with engine.connect() as connection: #The Connect Method Is Used To Establish A Connection To The Database Using The Engine Object.
        connection.execute(text("SELECT 1")) # If The Connection Is Successful, It Will Execute A Simple SQL Query To Return 1 From The Database.

#     return True #If Python Returns True, The Connection Is Established 

# def create_test_table():# Function To Create A Test Table In The Database For Testing Purposes.
#     with engine.connect () as connection: #The Connect Method Is Used To Establish A Connection.
#         connection.execute( #Command To Execute A Raw SQL Query To Create A Test Table If It Does Not Already Exist.
#             text("""
#                 CREATE TABLE IF NOT EXISTS test_table 
#                 (id SERIAL PRIMARY KEY, 
#                 name VARCHAR(50))
#                 """))
#         connection.commit() #Command To Commit The Changes To The Database.

# def data_insertion_test_table(name: str):
#     with engine.connect() as connection:
#         connection.execute( #Command To Execute A Raw SQL Query To Insert Data Into The Test Table.
#             text("""
#                 INSERT INTO test_table (name) VALUES (:name)
#                 """),
#             {"name": name}
#         )
#         connection.commit()
