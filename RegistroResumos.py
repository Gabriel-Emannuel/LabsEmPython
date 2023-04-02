class RegistroResumos:
    
    def __init__(self, quantosResumos:int) -> None:
        self.temas:list[str]  = ['' for x in range(quantosResumos)]
        self.conteudos:list[str] = ['' for x in range(quantosResumos)]
        self.quantosResumos:int = 0
    
    def adiciona(self ,tema:str, conteudo:str) -> None:
        self.temas[self.quantosResumos % len(self.temas)] = tema
        self.conteudos[self.quantosResumos % len(self.conteudos)] = conteudo
        self.quantosResumos += 1
    
    def pegaResumos(self) -> list[str]:
        parTemaConteudo:list[str] = ['' for x in range(self.conta())]
        for i in range(self.conta()):
            parTemaConteudo[i] = f'{self.temas[i]}: {self.conteudos[i]}'
        return parTemaConteudo

    def conta(self) -> int:
        if (self.quantosResumos >= len(self.temas)):
            return len(self.temas)
        return self.quantosResumos
    
    def temResumo(self, tema:str) -> bool:
        for temaVez in self.temas:
            if temaVez == tema:
                return True
        return False
    
    def temasDisponíveis(self) -> list[str]:
        if (self.quantosResumos >= len(self.temas)):
            return self.temas
        temasDisponiveis:list[str] = ['' for x in range(self.quantosResumos)]
        for i in range(self.quantosResumos):
            temasDisponiveis[i] = self.temas[i]
        return temasDisponiveis

    
    def imprimeResumos(self) -> str:
        return f'- {self.conta()} resumo(s) cadastrado(s)\n'+'- '+' | '.join(self.temasDisponíveis())