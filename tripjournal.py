
class TripJournal():
    
    def __init__(self, idTgm):
        self.idTgm = idTgm
        self.step = 0
        self._from = ''
        self.to = ''
        self.date = ''
        self.hour = ''
        self.price = 0
        self.desc = ''
        self.steps = ("Desde donde","A donde","Fecha","Hora","Precio","Descripcion","Escribe End para finalizar")
        self.fields = {0 : self._from,
                1 : self.to,
                2 : self.date,
                3 : self.hour,
                4 : self.price,
                5: self.desc}

    def out(self):
        return self.steps[self.step]

    def input(self,data):
        self.fields[self.step]= data
        print(self.fields)
        self.step += 1

