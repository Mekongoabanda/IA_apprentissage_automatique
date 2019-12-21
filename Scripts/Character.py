
class character:

    def __init__(self, nom, prenom, age, profession, boost_moral):
      self.nom = nom
      self.prenom = prenom
      self.age = age
      self.profession = profession
      self.boost_moral = float(boost_moral)

    def __str__(self):
        return f" \n Nom : {self.nom} \n Prenom: {self.prenom} \n Age: {self.age}" \
               f" \n profession: {self.profession} \n boost moral : {self.boost_moral} "

    def __repr__(self):
      return {'name': self.nom, 'prenom': self.prenom}

    def getNom(self):
        return self.nom

    def getAge(self):
        return self.age

    def getPrenom(self):
        return self.prenom

    def getProfession(self):
        return self.profession

    def getBoostMoral(self):
        return self.boost_moral

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def setAge(self, age):
        self.age = age

    def setProfession(self, profession):
        self.profession = profession

    def setNom(self, boost_moral):
        self.boost_moral = boost_moral