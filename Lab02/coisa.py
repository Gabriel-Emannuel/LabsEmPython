from Descanso import Descanso
from RegistroTempoOnline import RegistroTempoOnline
from Disciplina import Disciplina
from RegistroResumos import RegistroResumos

def registrarTempoOnline() -> None: 
    tempoLP2:RegistroTempoOnline = RegistroTempoOnline("LP2", 30)
    tempoLP2.adicionaTempoOnline(10)
    print(tempoLP2.atingiuMetaTempoOnline())
    tempoLP2.adicionaTempoOnline(10)
    tempoLP2.adicionaTempoOnline(10)
    print(tempoLP2.atingiuMetaTempoOnline())
    tempoLP2.adicionaTempoOnline(2)
    print(tempoLP2.atingiuMetaTempoOnline())
    print(tempoLP2.toString())
    tempoP2:RegistroTempoOnline = RegistroTempoOnline("P2")
    print(tempoP2.toString())

def controlarDisciplina() -> None: 
    prog2:Disciplina = Disciplina("PROGRAMACAO 2")
    prog2.cadastraHoras(4)
    prog2.cadastraNota(1, 5.0)
    prog2.cadastraNota(2, 6.0)
    prog2.cadastraNota(3, 7.0)
    print(prog2.aprovado())
    prog2.cadastraNota(4, 10.0)
    print(prog2.aprovado())
    print(prog2.toString())

def registrarResumos():
    meusResumos:RegistroResumos = RegistroResumos(100)
    
    meusResumos.adiciona("Classes", "Classes definem um tipo e a base de código para criação de objetos.")
    meusResumos.adiciona("Tipo", "Identifica a semântica (operações e significados) de um conjunto de dados.")


    resumos:list[str] = meusResumos.pegaResumos()


    for i in range(len(resumos)):
        print(resumos[i])


    print('')
    print("Resumos: ")
    print(meusResumos.imprimeResumos())
    print(meusResumos.temResumo("Classes"))
    print(meusResumos.temResumo("Objetos"))

def registrarDescanso():
    descanso:Descanso = Descanso()
    print(descanso.getStatusGeral())
    descanso.defineHorasDescanso(30)
    descanso.defineNumeroSemanas(1)
    print(descanso.getStatusGeral())
    descanso.defineHorasDescanso(26)
    descanso.defineNumeroSemanas(2)
    print(descanso.getStatusGeral())
    descanso.defineHorasDescanso(26)
    descanso.defineNumeroSemanas(1)
    print(descanso.getStatusGeral())

def main():
    registrarDescanso()
    print("-----")
    registrarTempoOnline()
    print("-----")
    controlarDisciplina()
    print("-----")
    registrarResumos()

main()