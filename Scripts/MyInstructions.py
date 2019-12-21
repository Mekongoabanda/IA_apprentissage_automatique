
import csv
import random
import cv2

import Army
import Character
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np


character_list = []
personnage1 = []
personnage2 = []
personnage3 = []
personnage4 = []
personnage5 = []
army1 = []
army2 = []
army3 = []
army4 = []
army5 = []


#Chemin de notre fichier
chemin1 = r"C:\Users\HP\PycharmProjects\TD1_naudin\Scripts\characters.csv"
with open(chemin1, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
            character_list.append(row)

character_list.remove(character_list[0])
print(character_list)


# ---------------------------------------------- Création de nos personnages et de leur armées --------------------------------------------------------
#Notre tableau est multidimensionnel donc "i" représente l'indice du tableau contenant les infos d'un personnage
# et "x" celui qui permet le parcours de chaque information
for i in range(len(character_list)):
    if i == 0:
        personneObjet = Character.character(character_list[i][0],character_list[i][1], character_list[i][2], character_list[i][3], character_list[i][4] )
        personnage1 = personneObjet
        # La valeur morale est un flottant aléatoire entre 20 et 100
        valeur_morale = random.uniform(0, 10)
        armyObject = Army.army(personnage1, valeur_morale)
        army1 = armyObject

    elif i == 1:
        personneObjet = Character.character(character_list[i][0], character_list[i][1], character_list[i][2],
                                                character_list[i][3], character_list[i][4])
        personnage2 = personneObjet
        # La valeur morale est un flottant aléatoire entre 20 et 100
        valeur_morale = random.uniform(0, 10)
        armyObject = Army.army(personnage2, valeur_morale)
        army2 = armyObject

    elif i == 2:
        personneObjet = Character.character(character_list[i][0], character_list[i][1], character_list[i][2],
                                                character_list[i][3], character_list[i][4])
        personnage3 = personneObjet
        # La valeur morale est un flottant aléatoire entre 20 et 100
        valeur_morale = random.uniform(0, 10)
        armyObject = Army.army(personnage3, valeur_morale)
        army3 = armyObject

    elif i == 3:
        personneObjet = Character.character(character_list[i][0], character_list[i][1], character_list[i][2],
                                                character_list[i][3], character_list[i][4])
        personnage4 = personneObjet
        # La valeur morale est un flottant aléatoire entre 20 et 100
        valeur_morale = random.uniform(0, 10)
        armyObject = Army.army(personnage4, valeur_morale)
        army4 = armyObject

    else:
        personneObjet = Character.character(character_list[i][0], character_list[i][1], character_list[i][2],
                                                character_list[i][3], character_list[i][4])
        personnage5 = personneObjet
        # La valeur morale est un flottant aléatoire entre 20 et 100
        valeur_morale = random.uniform(0, 10)
        armyObject = Army.army(personnage5, valeur_morale)
        army5 = armyObject

print(personnage1)
print(personnage2)
print(personnage3)
print(personnage4)
print(personnage5)

print(army1)
print(army2)
print(army3)
print(army4)
print(army5)

# TODO ------------------------------------- BOOST MORAL TOTAL 1 ------------------------------------------------------------------
army_total_value = Army.army.get_total_morale(self=army1) + Army.army.get_total_morale(self=army2) \
                   + Army.army.get_total_morale(self=army3) + Army.army.get_total_morale(self=army4) + Army.army.get_total_morale(self=army5)

print(f"\n La valeur total des valeur morales totales de toutes les Armée (première méthode) : {army_total_value}")

# TODO------------------------------------- BOOST MORAL TOTAL 2 -------------------------------------------------------------------
boost_moral_personnages = [Character.character.getBoostMoral(self=personnage1), Character.character.getBoostMoral(self=personnage2),
                           Character.character.getBoostMoral(self=personnage3), Character.character.getBoostMoral(self=personnage4),
                           Character.character.getBoostMoral(self=personnage5)]
valeur_morale_army =  [Army.army.getMoralValue(self=army1),Army.army.getMoralValue(self=army2),Army.army.getMoralValue(self=army3),
                       Army.army.getMoralValue(self=army4), Army.army.getMoralValue(self=army5) ]
boost_moral_totale = 0.0

for i in range(5):
    boost_moral_totale = boost_moral_totale +  boost_moral_personnages[i] * valeur_morale_army[i]
    print(f" Boost morale totale de l'armée n° {int(i+1)} : { boost_moral_personnages[i] * valeur_morale_army[i] }")

print( f"La valeur total des valeur morales totales de toutes les Armée (deuxième méthode) : {boost_moral_totale} ")

#TODO ---------------------------------------------  PREMIER RESEAU DE NEURONNES ---------------------------------------------------------------------------
# a = inputs, w = les poids, T la fonction d'activation et y =  la sortie
#T est la fonction qui à x associe 0 si x <=0,sinon 1
#On crée un tableau qui contient les possibilité dont une valeur de AND dispose
And_possibilities = [[0, 0], [0, 1], [1, 0], [1, 1]]
#notre tableau pour faire varier w1 et w2
tab_varie = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#Sorties attendues pour chaque paire d'input
exit_input = [0, 0, 0, 1]
variant = 0
#Variable de notre fonction
w1 = -5
w2 = -5
expected_release = 0
#lignes, colonnes = 10, 10
#tab_values_error = [[0] * colonnes] * lignes
tab_values_error = np.zeros((11,11))
receptacle = []
error_value = 0
total_error_value = 0
etape = 0
#Variation de w1 [-5;5], même chose pour w2
for i in range(11):
    w1 = tab_varie[i]
    for r in range(11):
        w2 = tab_varie[r]
        print(f"------------------- ETAPE {etape} PERCEPTRONS --------------------------")
        for z in range(4):
            calcul_percep = w1*And_possibilities[z][0] + w2*And_possibilities[z][1]
            print(f" calcul du perceptron (w1 = {w1} & w2 = {w2}) : {calcul_percep} ")
            t = exit_input[z]
            print(f"sortie t = {t}")
            if z<=3:
                if calcul_percep <= 0:
                    y = 0
                    print(f" Calcul n°{z} : Le neuronne ne s'active pas!!")
                    error_value = 0.5* (pow( (y - t), 2))
                    total_error_value += error_value
                    print(f" + Valeur d'erreur : {error_value}")
                else:
                    y = 1
                    print(f" Calcul n°{z} : Le neuronne s'active !")
                    error_value = 0.5* (pow( (y - t), 2))
                    total_error_value += error_value
                    print(f" + Valeur d'erreur : {error_value}")

            else:
                break
        print(f" Valeur totale d'erreur = {total_error_value}")
        #tab_values_error.append(total_error_value)
        tab_values_error[i][r] = total_error_value
        total_error_value = 0
        etape = len(tab_values_error)


# todo --------------------------------------------------------------------------------------------------------------------------------------

print("---------------------------------------------------- TABLEAU CONTENANT NOS VALEURS D'ERREUR -------------------------------------------------------------------")
print()
for i in range(10):
    print(tab_values_error[i])

plt.imshow(tab_values_error)
plt.title("SURFACE D'ERREUR EN IMAGE")
plt.ylabel("W1[0] à W1[10]")
plt.xlabel("W2[0] à W2[10]")
plt.show()
#img = cv2.imread(r'C:\Users\HP\PycharmProjects\TD1_naudin\denisenaafa.jpg', -1)
#cv2.imshow('image', img)
#plt.imshow(img)
#plt.show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()

""" #Stockage des données dans le fichier CSV
character_list.append(Character.character.getNom(self=ch))
character_list.append(Character.character.getPrenom(self=ch))
character_list.append(Character.character.getAge(self=ch))
character_list.append(Character.character.getBoostMoral(self=ch))
character_list.append(Character.character.getProfession(self=ch)) """

"""
with open(chemin1, "a", encoding='utf-8') as f:
    f.write(f"\n")
    for i in range(len(character_list)):
 #"w" pour formater et ecrire, "a" pour ajouter des mots existants
        f.write(f"{character_list[i]} ," ) """