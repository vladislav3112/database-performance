import sqlalchemy as db
from sqlalchemy import create_engine
import time
import os

DATABASE_PASSWORD = os.environ.get('PASSWORD')
DATABASE_URL =  os.environ.get('DATABASE_URL')
#engine = create_engine('mysql://root:' + DATABASE_PASSWORD + '@localhost/mydb', echo=False) #local
#engine = create_engine('mysql+mysqlconnector://root:example@localhost:3306/database') # for docker
engine = create_engine(DATABASE_URL) #heroku
metadata = db.MetaData()
connection = engine.connect()
user = db.Table('user', metadata, autoload=True, autoload_with=engine)

start = time.time()
results = connection.execute(db.select([user])).fetchall()
end = time.time()
print("Time of reading 1000 entries locally: ",end-start," s")
#df = pd.DataFrame(results)
#df.columns = results[0].keys()
#print(df.head(4))