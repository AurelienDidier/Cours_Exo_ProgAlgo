import random
from select import select


class Personnage:

    niveauMax = 99 #propriété statique

    def __init__(self, niveau=1, force=10, hp=100, hpMax=100, defense=10, Mort=10 ):
        self.__niveau = niveau #attributs privés
        self.__force = force
        self.__hp = hp
        self.__hpMax = hpMax
        self.__arme = Arme()
        self.__defense = defense
        self.__Mort = Mort 

    def equiper(self, arme):
        self.__arme = arme

    def getForce(self):
        return self.__force

    def getHP(self):
        return self.__hp

    def setHP(self, hp):
        self.__hp = hp

    def lvlUp(self):
        self.__niveau += 1
        self.__force += 2
        self.__hpMax += 20

    def estVivant(self):
        return self.__hp>0

    def attaquer(self, ennemie):
        ennemie.__hp -= ( self.__force * self.__arme.getDegat() ) - ennemie._defense
    
    def sortSoin (self):
        self.__defense +=10

class Mage (Personnage):

    def __init__(self):
        super().__init__() #réutilise le constructeur de la super classe Personnage
        self.__magie = 5

    def lvlUp(self):
        """
        self.__niveau += 1
        self.__force += 2
        self.__hpMax += 20
        """
        super().lvlUp()
        self.__magie +=2

    def attaquer(self, ennemie):
        ennemie.setHP(ennemie.getHP() - (self.getForce() + self.__magie) * self.__arme.getDegat())

    def equiper (self, arme):
        if isinstance(arme, Baton):
            self.__arme = arme

class Arme:

    def __init__(self, degatArme = 1):
        self.__degat = degatArme

    def getDegat(self):
        return self.__degat

class Baton(Arme):

    def __init__(self, degatArme = 2):
        super().__init__(degatArme)
        self.type = "Feu"

class RPG:

    def playGame():
        heros = Personnage()
        mechant = Mage()

        epee = Arme(5)
        heros.equiper(epee)

        baton = Baton(10)
        mechant.equiper(baton)

        heros.lvlUp()

        Mort = Mort ()

#       print(Personnage.niveauMax)#appel d'une propriété statique      
        while mechant.estVivant() and heros.estVivant():
            temp = input("choisissez entre 'attaquer', 'soins' ")
            if temp == 'attaquer':
                heros.attaquer(mechant)
            elif temp == 'soins':
                heros.sortSoin()
                mechant.attaquer(heros)

        select = random.randint()

        if (heros.estVivant()):
            heros.lvlUp()
            print("Le héros a gagné!")
            print('gagner des butins a la fin de chaque combat ')
            
        else:
            mechant.lvlUp()
            print ("Le méchant a gagné!")
            print('gagner des butins a la fin de chaque combat ')
        
        
RPG.playGame() 