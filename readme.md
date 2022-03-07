###  Отчет (тест для 1000 записей)   
###  docker-compose  up to run database in container
####  Запись локально  0.37 - сек  
####  Чтение локально  0.016 - сек  
####  Чтение через heroku  0.01 - сек  
####  Запись через heroku  0.37 - сек  
####  Запись через docker  0.32 - сек
####  Запись через docker  0.015 - сек
####  Чтение локально  0.01 - сек  

config = {
    "drivername": "mysql+mysqlconnector",
    "username": "root",
    "password": "example",
    "host": "localhost",
    "port": "3308",
    "database": "database",
}
#192.168.31.144
#engine = create_engine('mysql://root:' + DATABASE_PASSWORD + '@localhost/mydb', echo=False)
engine = create_engine(engine.url.URL.create(**config)) #for docker
