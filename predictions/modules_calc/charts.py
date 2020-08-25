import csv
import matplotlib.pyplot as plt

def Generate_chart():

    list_x = []
    list_y = []
    with open('predictions/analisis.csv') as CSVfile:
        reader = csv.DictReader(CSVfile)

        for row in reader:
            list_x.append(float(row['Horas de estudio']))
            list_y.append(float(row['Calificacion obtenida']))

    plt.scatter(list_x,list_y, s=80, facecolors= 'none', edgecolors='r')

    plt.show()

