from datetime import datetime

class Employe:
    def __init__(self, numero, nom, qualification, dateEmbauche):
        self.numero = numero
        self.nom = nom
        self.qualification = qualification
        self.dateEmbauche = datetime.strptime(dateEmbauche, '%d/%m/%Y')
        
    def coutHoraire(self):
        anciennete = self.getAnciennete()
        coefficient = 1
        if anciennete >= 5 and anciennete <= 10:
            coefficient = 1.05
        elif anciennete >= 11 and anciennete <= 15:
            coefficient = 1.08
        elif anciennete > 15:
            coefficient = 1.12
        return self.qualification.tauxHoraire() * coefficient
        
    def getNumero(self):
        return self.numero
    
    def getNom(self):
        return self.nom
    
    def getQualification(self):
        return self.qualification
    
    def getDateEmbauche(self):
        return self.dateEmbauche
    
    def getAnciennete(self):
        delta = datetime.now() - self.dateEmbauche
        return int(delta.days / 365)