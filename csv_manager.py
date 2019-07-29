import csv
from manipulator import Manipulator

class CSV_Manager:
    def __init__(self, filename):
        self.filename = filename

    def get_csv_as_dicts(self):
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = [row for row in csv_reader]
            return self.to_dict(rows)

    def to_dict(self, rows):
        keys = rows[0]
        all_data = []

        for row in rows:
            data_dict = {}
            for i in range(0, len(row)):
                data_dict[keys[i]] = row[i]
            all_data.append(data_dict)

        return all_data
    def map_author(self):
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = [row for row in csv_reader]
        articles = self.get_csv_as_dicts()
        manipulator = Manipulator(articles)
        a = {}
        b = rows.pop(0)
        for x in range(4):
            for j in rows:
                a[j[x]] = manipulator.filter_by(b[x], j[x])
        return a