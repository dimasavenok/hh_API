import json

from src.storage.DBManager import DBManager

# connect_params = {
#     "dbname": "hh_db",
#     "user": "postgres",
#     "password": "hh_password",
#     "host": "localhost",
#     "port": "5432"
# }
with open("params.json", mode="r", encoding="UTF-8") as file:
    connect_params = json.load(file)
db: DBManager = DBManager(connect_params)
# db.insert_company("K-test")
# db.insert_vacancy(
#     title="py",
#     salary=100,
#     url="ddddd",
#     description="fffff",
#     company_name="K-test"
# )
