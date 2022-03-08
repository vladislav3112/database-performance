import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine, engine
import time
import os

DATABASE_PASSWORD =  os.environ.get('DATABASE_PASSWORD')
Faker.seed(1) #makes datgen reproductive

fake = Faker()
fake_data = defaultdict(list)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
for _ in range(1000):
    fake_data["first_name"].append( fake.first_name() )
    fake_data["last_name"].append( fake.last_name() )
    fake_data["occupation"].append( fake.job() )
    fake_data["dob"].append( fake.date_of_birth() )
    fake_data["country"].append( fake.country() )
df_fake_data = pd.DataFrame(fake_data)
#engine = create_engine('mysql://root:' + DATABASE_PASSWORD + '@localhost/mydb', echo=False) - local
#engine = create_engine('mysql+mysqlconnector://root:example@localhost:3306/database') - docker
engine = create_engine(SQLALCHEMY_DATABASE_URI) #heroku
start = time.time()
df_fake_data.to_sql('user', con=engine,index=False)
end = time.time()
print("Time of writing 1000 entries locally: ",end-start," s")