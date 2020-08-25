import math, csv

def covariance():
    lista_result_x = []
    lista_result_y = []

    lista_difference_x = []
    lista_difference_y = []


    with open('predictions/analisis.csv') as CSV_file:
        reader = csv.DictReader(CSV_file)

        for row in reader:
            lista_result_x.append(float(row['Horas de estudio']))
            lista_result_y.append(float(row['Calificacion obtenida']))
        
    average_x = "{0:.2f}".format(((sum(lista_result_x))/len(lista_result_x)))
    average_x = float(average_x)
    
    average_y = "{0:.2f}".format(((sum(lista_result_y))/len(lista_result_y)))
    average_y = float(average_y)
    
    # here we get difference between X and her X media
    # Also Y - Y media x
    for x in lista_result_x:
        difference_x = "{0:.2f}".format(x - average_x) # format 2 decimals
        difference_x =  float(difference_x) # convert to float type
        lista_difference_x.append(difference_x)
    
    for y in lista_result_y:
        difference_y = "{0:.2f}".format(y - average_y)
        difference_y =  float(difference_y)
        lista_difference_y.append(difference_y)


    sum_total = 0
    
    for i in range(0,10):
        
        sum_total = sum_total + (lista_difference_x[i] * lista_difference_y[i])

    covarianza = sum_total / (len(lista_result_x) - 1)
    covarianza_result = "{0:.2f}".format(covarianza)

    covarianza_result = float(covarianza_result)

    return covarianza_result
    # after we obtain those values, apply Covariance Formula.


# B0
def population_intersection(): 
    lista_result_x = []
    lista_result_y = []

    lista_difference_x = []
    lista_difference_y = []


    with open('predictions/analisis.csv') as CSV_file:
        reader = csv.DictReader(CSV_file)

        for row in reader:
            lista_result_x.append(float(row['Horas de estudio']))
            lista_result_y.append(float(row['Calificacion obtenida']))
        
    average_x = "{0:.2f}".format(((sum(lista_result_x))/len(lista_result_x)))
    average_x = float(average_x)
    
    average_y = "{0:.2f}".format(((sum(lista_result_y))/len(lista_result_y)))
    average_y = float(average_y)
    
    # here we get difference between X and her X media
    # Also Y - Y media x
    for x in lista_result_x:
        difference_x = "{0:.2f}".format(x - average_x) # format 2 decimals
        difference_x =  float(difference_x) # convert to float type
        lista_difference_x.append(difference_x)
    
    for y in lista_result_y:
        difference_y = "{0:.2f}".format(y - average_y)
        difference_y =  float(difference_y)
        lista_difference_y.append(difference_y)


    sum_total = 0
    sum_pow = 0

    for i in range(0,10):
        
        sum_total = sum_total + (lista_difference_x[i] * lista_difference_y[i])


    for x_sum in lista_difference_x:
        sum_pow = sum_pow + pow(x_sum, 2)



    interception_beta_one = sum_total / sum_pow
    B1 = "{0:.2f}".format(interception_beta_one)
    B1 = float(B1)
    return B1


def population_slop(): #B1

    lista_result_x = []
    lista_result_y = []

    with open('predictions/analisis.csv') as CSV_file:
        reader = csv.DictReader(CSV_file)

        for row in reader:
            lista_result_x.append(float(row['Horas de estudio']))
            lista_result_y.append(float(row['Calificacion obtenida']))
        
    average_x = "{0:.2f}".format(((sum(lista_result_x))/len(lista_result_x)))
    average_x = float(average_x)
    
    average_y = "{0:.2f}".format(((sum(lista_result_y))/len(lista_result_y)))
    average_y = float(average_y)

    B1 = population_intersection()

    interception_beta_zero_result = ((average_y) - (average_x * B1))

    B0 = "{0:.2f}".format(interception_beta_zero_result)
    B0 = float(B0)

    return B0

def min():
    lista_sorted = []

    with open('predictions/analisis.csv') as CSVfile:
        reader = csv.DictReader(CSVfile)

        for rows in reader:
            #print(rows['Horas de estudio'])
            lista_sorted.append(int(rows['Horas de estudio']))

    lista_sorted.sort()

    return lista_sorted[0]


def max():
    lista_sorted = []
    
    with open('predictions/analisis.csv') as CSVfile:
        reader = csv.DictReader(CSVfile)

        for rows in reader:
            #print(rows['Horas de estudio'])
            lista_sorted.append(int(rows['Horas de estudio']))

    lista_sorted.sort()
    quntity = len(lista_sorted)
    return lista_sorted[quntity - 1]