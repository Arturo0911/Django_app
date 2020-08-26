import csv

list_x = []
list_y = []


def _get_lists_x():

    with open('predictions/analisis.csv') as CSVfile:
        reader = csv.DictReader(CSVfile)

        for row in reader:
            list_x.append(float(row['Horas de estudio']))
    
    return list_x

def _get_lists_y():
    
    with open('predictions/analisis.csv') as CSVfile:
        reader = csv.DictReader(CSVfile)

        for row in reader:
            list_y.append(float(row['Calificacion obtenida']))

    return list_y