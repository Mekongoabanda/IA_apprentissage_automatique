import csv
import random
import cv2

import Army
import Character
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from Scripts import Perceptron

#------------------------------------------------------ FONCTIONS -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def saveInputOutput_7segment():
    Input_7Segment = [[0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1, 1],
                      [1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0, 1], [1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 0, 1, 1]]

    Output_7segment = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    with open('input7Segment.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(Input_7Segment)):
            spamwriter.writerow(Input_7Segment[i])

    with open('output7Segment.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(Output_7segment)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

cheminInput  = r"C:\Users\HP\PycharmProjects\TD1_naudin\Scripts\input7Segment.csv"
cheminOutput =  r"C:\Users\HP\PycharmProjects\TD1_naudin\Scripts\output7Segment.csv"
Input_7Segment = []
Output_7segment = []
saveInputOutput_7segment()

with open(cheminInput, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        Input_7Segment.append(row)

with open(cheminOutput, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        Output_7segment.append(row)

#On caste nos chaînes de cararctères en int
Input_7Segment = [list(map(int, l)) for l in Input_7Segment]
Output_7segment = list(map(int, Output_7segment[0]))

#Chemin de notre fichier
chemin1 = r"C:\Users\HP\PycharmProjects\TD1_naudin\Scripts\poids.csv"
#Sorties attendues pour chaque paire d'input
exit_input = [0, 0, 0, 1]
#On crée un tableau qui contient les possibilité dont une valeur de AND dispose
And_possibilities = [[0, 0], [0, 1], [1, 0], [1, 1]]


with open('poids.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['W0 ', 'W1 ', 'W2 '])

mPerceptronClass = Perceptron.perceptron(2, 10, 0.001, False)

if mPerceptronClass.RuleAtication :
    mPerceptronClass.train(And_possibilities, exit_input)
    mPerceptronClass.load_weigths(chemin1)
else:
    print(
        f" \n \n-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("*")
    print("*                                                             AFFICHEUR 7 SEGMENT")
    print("*")
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------------")

    print(f" \nFORMATION DES INPUTS (allumé à 1 et éteind à 0) : {Input_7Segment}")
    print(f"  TAILLE DES INPUTS : {len(Input_7Segment)}")
    print(f" \n FORMATION DES OUTPUTS (Nombre affiché dans l'afficheur 7-Segment) : {Output_7segment}")
    print(f"  TAILLE DES OUTPUTS : {len(Output_7segment)} ")
    mPerceptronClass.train(Input_7Segment, Output_7segment)
    mPerceptronClass.load_weigths(chemin1)



