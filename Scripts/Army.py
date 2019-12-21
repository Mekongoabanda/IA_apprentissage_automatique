import Character


class army:

    def __init__(self, chef, moral_value):
        self.chef = chef
        self.moral_value = moral_value

    def __str__(self):
        return f"Chef: {Character.character.getNom(self=self.chef)}" \
               f" {Character.character.getPrenom(self=self.chef)} \n Valeur moral de l'armée : {self.moral_value}"

    def get_total_morale(self):
        return self.moral_value * Character.character.getBoostMoral(self=self.chef)


    def getChef(self):
        return self.chef

    def getMoralValue(self):
        return self.moral_value

    def setChef(self, chef):
        self.chef = chef

    def setMoralValue(self, moral_value):
        self.moral_value = moral_value
