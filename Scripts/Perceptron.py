import csv
import random
import cv2

import Army
import Character
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class perceptron:
    biais = 1
    erreur = 0
    tabError_total_epoch = []
    w3 = 0  # poids w1 initialisé à 0
    w4 = 0  # poids w2 initialisé à 0
    w5 = 0  # poids w0 initialisé à 0
    w6 = 0  # poids w1 initialisé à 0
    w7 = 0  # poids w2 initialisé à 0

    def __init__(self, nombre_input, nbre_LearningLoop, learningRate, RuleActivation ):
        self.nombre_input =  nombre_input #nombre_d'input du perceptrons
        self.nombre_LearningLoop = nbre_LearningLoop  #nombre de boucle d'apprentissage
        self.learningRate = learningRate #Taux d'apprentissage
        self.w1 = 0 #poids w1 initialisé à 0
        self.w2 = 0  #poids w2 initialisé à 0
        self.w0 = 0  #poids w0 initialisé à 0
        self.RuleAtication = RuleActivation

    def save_weights(self):
        #On enregistre les valeurs des poids pour chaque paire d'inputs
        with open('poids.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([self.w0, self.w1, self.w2])

    def load_weigths(self, chemin):
        poids_list = []
        with open(chemin, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                poids_list.append(row)

        poids_list.remove(poids_list[0])
        print(poids_list)
        return poids_list

    #Méthode qui prend en argument une paire d'inputs et qui retourne 1 ou 0
    def predict(self, paire_inputs):
        calcul_percep = self.w1 * paire_inputs[0] + self.w2 * paire_inputs[1] + self.w0 * self.biais
        if calcul_percep <= 0 :
            return 0
        else:
            return 1

    def ReLu(self, inputs ):
        calcul_percep = self.w1 * inputs[0] + self.w2 * inputs[1] + \
                        self.w3 * inputs[2] + self.w4 * inputs[3] + \
                        self.w5 * inputs[4] + self.w6 * inputs[5] + \
                        self.w7 * inputs[6] + self.w0 * self.biais
        if calcul_percep <= 0 :
            return 0
        else:
            return calcul_percep

    def train(self, input_possibilities, exit_possibilities):

        for j in range (self.nombre_LearningLoop) :
            valueTotalError = 0
            print()
            print(f"------------------------------- BOUCLE D'APPRENTISSAGE {j+1} -----------------------------------------------------")
            for i in range(len(input_possibilities)):
                self.save_weights()
                if self.RuleAtication:
                    y = self.predict(input_possibilities[i])
                else :
                    y = self.ReLu(input_possibilities[i])
                    self.w3 = self.w1 + self.learningRate * (exit_possibilities[i] - y) * input_possibilities[i][2]
                    self.w4 = self.w2 + self.learningRate * (exit_possibilities[i] - y) * input_possibilities[i][3]
                    self.w5 = self.w1 + self.learningRate * (exit_possibilities[i] - y) * input_possibilities[i][4]
                    self.w6 = self.w2 + self.learningRate * (exit_possibilities[i] - y) * input_possibilities[i][5]
                    self.w7 = self.w1 + self.learningRate * (exit_possibilities[i] - y) * input_possibilities[i][6]
                if y == 0:
                    print(f" ******************************* LE NEURONNE NE S'ACTIVE PAS *********************************")
                else:
                    print(f" ******************************* ACTIVATION DU NEURONNE *********************************")
                print(f"  predict : {y} ")
                self.erreur = 0.5 * (pow((y - exit_possibilities[i]), 2))
                print(f" + Valeur d'erreur : {self.erreur}")
                self.w1 = self.w1 + self.learningRate * (exit_possibilities[i] - y) * input_possibilities[i][0]
                self.w2 = self.w2 + self.learningRate * (exit_possibilities[i] - y) * input_possibilities[i][1]
                self.w0 = self.w0 + self.learningRate * (exit_possibilities[i] - y) * self.biais
                print(f"  valeur de W1 : {self.w1} ")
                print(f"  valeur de W2 : {self.w2} ")
                print(f"  valeur de W0 : {self.w0} ")
                valueTotalError = valueTotalError + self.erreur

            self.tabError_total_epoch.append(valueTotalError)
            print(f"  Total des erreurs : {valueTotalError} ")
        plt.plot(self.tabError_total_epoch, '-.', color="red", lw=2)
        plt.title("SURFACE D'ERREUR DES EPOCH")
        plt.xlabel(f"NOMBRE D'EPOCHES = {self.nombre_LearningLoop}")
        plt.ylabel(f"VALEURS D'ERREUR")
        plt.show()









