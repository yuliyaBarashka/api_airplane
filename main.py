from services.data_loader import init_countries, load_airplanes
from db.db_manager import DBManager

init_countries()
load_airplanes()

db = DBManager()

print(db.get_countries_and_aeroplanes_count())
print(db.get_avg_speed())
print(db.get_aeroplanes_with_higher_speed())
print(db.get_aeroplanes_with_keyword("ACA"))

db.close()
