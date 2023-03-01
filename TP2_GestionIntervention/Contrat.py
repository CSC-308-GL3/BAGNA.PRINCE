from datetime import datetime

class Contrat:
    def __init__(self, numero, date, client, montantContrat):
        self.numero = numero
        self.date = datetime.strptime(date, '%d/%m/%Y')
        self.client = client
        self.montantContrat = montantContrat
        self.interventions = []
        self.nbIntervention = 0
        
    def montant(self):
        return self.montantContrat