import sqlalchemy as db
from sqlalchemy import create_engine
import time
import os

DATABASE_PASSWORD = os.environ.get('PASSWORD')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
#engine = create_engine('mysql://root:' + DATABASE_PASSWORD + '@localhost/mydb', echo=False) #local
#engine = create_engine('mysql+mysqlconnector://root:example@localhost:3306/database') # for docker
engine = create_engine(SQLALCHEMY_DATABASE_URI) #heroku
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