
class TripJournal():
    String _from
    def __init__(self, idTgm):
        self.idTgm = idTgm
        self.step = 0
        
        self.steps = { 
                0 : "Desde donde",
                1 : "A donde",
                2 : "Fecha",
                3 : "Hora",
                4 : "Precio",
                5 : "Descripcion"
                }
        self.fields = {0 : self._from,
                1 : to,
                2 : date,
                3 : hour,
                4 : price,
                5: desc}

    def out(self):
        return self.steps[self.step]

    def input(self,data):
        self.fields[step]= data
        
        self.step += 1

tp = TripJournal(123)
print(tp.out())
tp.input('Zaragoza')
print(tp.out())
tp.input('Madrid')
print(tp.out())



