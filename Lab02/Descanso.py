class Descanso:
    
    def __init__(self) -> None:
        self.horasDescanso:int = 0
        self.numerosSemanas:int = -1

    def getStatusGeral(self) -> str:
        estaDescansado: bool = (self.horasDescanso // self.numerosSemanas >= 26)
        if (estaDescansado):
           return 'descansado'
        else:
            return 'cansado'
    
    def defineHorasDescanso(self ,horas:int) -> None:
        self.horasDescanso = horas
        return None
    
    def defineNumeroSemanas(self, semanas:int) -> None:
        self.numerosSemanas = semanas
        return None