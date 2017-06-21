
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
        self.steps = { 
                0 : "Desde donde",
                1 : "A donde",
                2 : "Fecha",
                3 : "Hora",
                4 : "Precio",
                5 : "Descripcion"
                }
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
        
        self.step += 1

tp = TripJournal(123)
print(tp.out())
tp.input('Zaragoza')
print(tp.out())
tp.input('Madrid')
print(tp.out())



