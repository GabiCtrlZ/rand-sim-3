from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def run(filter_field, value = None):
    reader = CSV_Manager("./articles.csv")
    if value != None:
        articles = reader.get_csv_as_dicts()
        manipulator = Manipulator(articles)

        filtered = manipulator.filter_by(filter_field, value)
        print(json.dumps(filtered, indent=2))
    else:
        a = reader.map_author()
        print(json.dumps(a[filter_field], indent=2))

    
    

run("a1")
run("author", "a1")