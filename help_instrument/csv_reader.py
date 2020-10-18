import csv
from ship import Ship
def read_file_csv(file_name):
    list_of_ships = []
    with open(file_name, 'r') as csv_file:

        reader = csv.reader(csv_file)
        for row in reader:
            list_of_ships.append(Ship(row[0], int(row[1]), int(row[2])))
        return list_of_ships

