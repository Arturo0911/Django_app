import csv

def _initialize():

    with open('predictions/analisis/articulos_ml.csv') as CSVfile:
        reader = csv.DictReader(CSVfile)

        for row in reader:
            print(row['# Shares'])
    return True