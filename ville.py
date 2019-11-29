class ville:
    def __init__(self, nom, nbHabitants=0):
        self.nom = nom.upper()
        self.nbHabitants = nbHabitants
        self.categorie = ""

    def get__nom(self):
        return self.nom

    def get__nbHabitants(self):
        return self.nbHabitants

# Si la valeur transmise est négative on renvoi 0. Sinon on renvoi le nb saisi
    def set__nbHabitants(self, nb):
        if nb < 0:
            self.nbHabitants = 0
        else:
            self.nbHabitants = nb

# Si le nb d'habitants est différent de 0 (donc on le connait) alors on renvoi True
    def nbHabitantsConnus(self):
        if self.nbHabitants == 0:
            return False
        else:
            return True

# Test le nb d'habitants pour établir la catégorie. Le test nbHabitants == 0 va en 2ème position car en dernière position il n'était jamais utilisé
    def categories(self):
        if "pays" in self.__dict__:
            self.categorie = "C"
        elif self.nbHabitants == 0:
            self.categorie = "?"
        elif self.nbHabitants < 500001:
            self.categorie = "A"
        elif self.nbHabitants > 499999:
            self.categorie = "B"



    def __str__(self):
        return "Ville de {} ; {} habitants.".format(self.get__nom(), self.get__nbHabitants())

# Test
# ville1 = ville("Paris", 15257829)
# print(ville1)


class capitale(ville):
    def __init__(self, pays, nom, nbHabitants=0):
        ville.__init__(self, nom, nbHabitants)
        self.pays = pays.upper()

    def __str__(self):
        return "Ville de {} ; {} habitants ; categorie {}".format(self.get__nom(), self.get__nbHabitants(), self.categorie)


paris = capitale('france', 'Paris', 2181371)
paris.categories()
strasbourg = ville('StrasBourg', 272975)
strasbourg.categories()
toulouse = ville('ToulousE')
toulouse.categories()
rome = capitale('rome', 'italie', 2700000)
rome.categories()

print('Ville de {}.'.format(toulouse.nom))
print('Ville de {} ; {} habitants.'.format(strasbourg.nom, strasbourg.nbHabitants))
print('Ville de {} ; {} habitants. Capitale de {}.'.format(paris.nom, paris.nbHabitants, paris.pays))
print('Ville de {} ; {} habitants. Capitale de {}.'.format(rome.nom, rome.nbHabitants, rome.pays))
print('catégorie de la ville de {} : {}'.format(toulouse.nom, toulouse.categorie))
print('catégorie de la ville de {} : {}'.format(strasbourg.nom, strasbourg.categorie))
print('catégorie de la ville de {} : {}'.format(paris.nom, paris.categorie))