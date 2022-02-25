import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine
import time
import os

fake = Faker()
DATABASE_PASSWORD = os.environ.get('PASSWORD')
Faker.seed(1) #makes datgen reproductive

fake_data = defaultdict(list)

for _ in range(1000):
    fake_data["first_name"].append( fake.first_name() )
    fake_data["last_name"].append( fake.last_name() )
    fake_data["occupation"].append( fake.job() )
    fake_data["dob"].append( fake.date_of_birth() )
    fake_data["country"].append( fake.country() )
df_fake_data = pd.DataFrame(fake_data)

engine = create_engine('mysql://root:' + DATABASE_PASSWORD + 'localhost/mydb', echo=False)

start = time.time()
df_fake_data.to_sql('user', con=engine,index=False)
end = time.time()
print("Time of writing 1000 entries locally: ",end-start," s")