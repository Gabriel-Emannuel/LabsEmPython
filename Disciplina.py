class Disciplina:

    def __init__(self, nome:str) -> None:
        self.nomeDisciplina:str = nome
        self.horasEstudos:int = 0
        self.Notas:list[float] = [0, 0, 0 ,0]
    
    def cadastraHoras(self, horas:int) -> None:
        self.horasEstudos += horas
    
    def cadastraNota(self, indice:int, nota: float) -> None:
        self.Notas[indice-1] = nota
    
    def media(self) -> float:
        soma:int = 0
        for i in range(4):
            soma += self.Notas[i]
        return soma / 4

    def aprovado(self) -> bool:
        estaAprovado:bool = (self.media() >= 7)
        return estaAprovado

    def toString(self) -> str:
        return f'{self.nomeDisciplina} {self.horasEstudos} {self.media()} {self.Notas}'
