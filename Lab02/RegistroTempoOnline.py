class RegistroTempoOnline:

    def __init__(self, nome:str, tempoEsperado:int = 120) -> None:
        self.nomeDisciplina: str = nome
        self.tempoOnline:int = 0
        self.tempoEsperado:int = tempoEsperado
    
    def adicionaTempoOnline(self, tempo:int) -> None:
        self.tempoOnline += tempo
    
    def atingiuMetaTempoOnline(self) -> bool:
        atingiuMeta:bool = (self.tempoOnline >= self.tempoEsperado)
        return atingiuMeta

    def toString(self) -> str:
        return f'{self.nomeDisciplina} {self.tempoOnline}/{self.tempoEsperado}'