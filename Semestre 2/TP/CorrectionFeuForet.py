import enum, random, copy

class Etat(enum.Enum):
     EnVie = 2
     EnFeu = 1
     EnCendre = 0

class Arbre:

    def __init__(self):
        self.__etat = Etat.EnVie

    def brule(self):
        if (self.__etat == Etat.EnVie):
            self.__etat = Etat.EnFeu

    def crame(self):
        if (self.__etat == Etat.EnFeu):
            self.__etat = Etat.EnCendre

    def getEtat(self):
        return self.__etat

    def __str__(self):
        if (self.__etat == Etat.EnFeu):
            return "*"
        elif (self.__etat == Etat.EnCendre):
            return "#"


class Bouleau(Arbre):

    def __init__(self):
        super().__init__()

    def __str__(self):
        if (self.getEtat() == Etat.EnVie):
            return "B"
        else :
            return super().__str__()
    
    def propage(self, foret, i, j):
        if (self.getEtat()==Etat.EnFeu):
            foret[i][j].crame()
            if (i>0 and j>0):
                foret[i-1][j-1].brule()
            if (i>0):
                foret[i-1][j].brule()
            if (i>0 and j<len(foret)-1):
                foret[i-1][j+1].brule()
            if (j>0):
                foret[i][j-1].brule()
            if (j<len(foret)-1):
                foret[i][j+1].brule()
            if (i<len(foret)-1 and j>0):
                foret[i+1][j-1].brule()
            if (i<len(foret)-1):
                foret[i+1][j].brule()
            if (i<len(foret)-1 and j<len(foret)-1):
                foret[i+1][j+1].brule()

class Chene(Arbre):

    def __init__(self):
        super().__init__()

    def __str__(self):
        if (self.getEtat() == Etat.EnVie):
            return "C"
        else :
            return super().__str__()

    def propage(self, foret, i, j):
        if (self.getEtat()==Etat.EnFeu):
            foret[i][j].crame()
            if (i>0):
                foret[i-1][j].brule()
            if (j>0):
                foret[i][j-1].brule()
            if (j<len(foret)-1):
                foret[i][j+1].brule()
            if (i<len(foret)-1):
                foret[i+1][j].brule()


class Sapin(Arbre):

    def __init__(self):
        super().__init__()

    def __str__(self):
        if (self.getEtat() == Etat.EnVie):
            return "S"
        else :
            return super().__str__()

    def propage(self,foret, i, j):
        if (self.getEtat()==Etat.EnFeu):
            foret[i][j].crame()
            if (i>0 and random.randint(0,1)==1):
                foret[i-1][j].brule()
            if (j>0 and random.randint(0,1)==1):
                foret[i][j-1].brule()
            if (j<len(foret)-1 and random.randint(0,1)==1):
                foret[i][j+1].brule()
            if (i<len(foret)-1 and random.randint(0,1)==1):
                foret[i+1][j].brule()

class Vide(Arbre):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return " "
        """
                if (self.getEtat() == Etat.EnVie):
                    return " "
                else :
                    return super().__str__()
        """
    def propage(self, foret, i, j):
        if (self.getEtat()==Etat.EnFeu):
            foret[i][j].crame()

class Foret:

    def __init__(self, pBouleau, pSapin, pChene, taille):
        self.arbres = []
        for i in range (0,taille):
            self.arbres.append([])
            for j in range (0,taille):
                alea = random.randint(0,100)
                if alea < pBouleau:
                    self.arbres[i].append(Bouleau())
                elif alea < pBouleau+pChene:
                    self.arbres[i].append(Chene())
                elif alea < pBouleau+pChene + pSapin:
                    self.arbres[i].append(Sapin())
                else:
                    self.arbres[i].append(Vide())

    def propage(self):
        cop = copy.deepcopy(self.arbres)
        for i in range (0, len(self.arbres)):
            for j in range(0,len(self.arbres)):
                self.arbres[i][j].propage(cop,i,j)
        self.arbres = cop

    def encoreEnFeu(self):
        for i in range (0, len(self.arbres)):
            for j in range(0,len(self.arbres)):
                if (self.arbres[i][j].getEtat()==Etat.EnFeu):
                    return True
        return False

    def afficheStats(self, step):
        count=0
        countB=0
        countC=0
        countS=0
        countV=0
        totalC=0
        totalS=0
        totalB=0
        totalV=0
        for i in range (0, len(self.arbres)):
            for j in range(0,len(self.arbres)):
                if (isinstance(self.arbres[i][j],Chene)):
                    totalC+=1
                if (isinstance(self.arbres[i][j],Bouleau)):
                    totalB+=1
                if (isinstance(self.arbres[i][j],Sapin)):
                    totalS+=1
                if (isinstance(self.arbres[i][j],Vide)):
                    totalV+=1

                if (self.arbres[i][j].getEtat()==Etat.EnCendre):
                    count+=1
                    if (isinstance(self.arbres[i][j],Chene)):
                        countC+=1
                    if (isinstance(self.arbres[i][j],Bouleau)):
                        countB+=1
                    if (isinstance(self.arbres[i][j],Sapin)):
                        countS+=1
                    if (isinstance(self.arbres[i][j],Vide)):
                        countV+=1
        print ("Le pourcentage d'arbre cram?? est: " + str(count*100/(len(self.arbres)**2)) +"%")
        print ("Le pourcentage de sapin cram?? est: " + str(100*countS/totalS) +"%")
        print ("Le pourcentage de bouleau cram?? est: " + str(100*countB/totalB) +"%")
        print ("Le pourcentage de chene cram?? est: " + str(100*countC/totalC) +"%")
        print ("Le pourcentage d'herbe cram?? est: " + str(100*countV/totalV) +"%")
        print ("La f??ret ?? brul?? en : " + str(step) +" ??tapes.")


    def allumeLeFeu(self,pos):
        self.arbres[pos][pos].brule()

    def __str__(self):
        ch = ""
        for i in range (0, len(self.arbres)):
            for j in range (0, len(self.arbres)):
                ch += str(self.arbres[i][j]) + " "
            ch += "\n"
        return ch


    
class Simulation:

    def run():
        f = Foret(20,20,30,20)
        f.allumeLeFeu(10)
        step = 0
        while(f.encoreEnFeu()):
            print(f)
            f.propage()
            step +=1
        f.afficheStats(step)
Simulation.run()
