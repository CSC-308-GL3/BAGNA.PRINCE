class Client:
    def __init__(self, numero, nom, adresse, codePostale, ville, nbKm):
        self.numero = numero
        self.nom = nom
        self.adresse = adresse
        self.codePostale = codePostale
        self.ville = ville
        self.nbKm = nbKm
        
    def distance(self):
        return self.nbKm