from datetime import datetime

class Intervention:
    def __init__(self, numero, date, duree, tarifKm, technicien):
        self.numero = numero
        self.date = datetime.strptime(date, '%d/%m/%Y')
        self.duree = duree
        self.tarifKm = tarifKm
        self.technicien = technicien
        
    def affiche(self):
        print("Intervention n°{} :".format(self.numero))
        print("Date : {}".format(datetime.strftime(self.date, '%d/%m/%Y')))
        print("Durée : {} heures".format(self.duree))
        print("Coût kilométrique : {} €/km".format(self.tarifKm))
        print("Technicien : {} ({})".format(self.technicien.getNom(), self.technicien.getQualification().getLibelle()))
        
    def fraisKm(self, dist):
        return self.tarifKm * dist
    
    def fraisMo(self):
        return self.duree * self.technicien.coutHoraire()