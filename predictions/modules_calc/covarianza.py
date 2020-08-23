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
    average_y = float(average_x)
    
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

    return covarianza_result
    # after we obtain those values, apply Covariance Formula.