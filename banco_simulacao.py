from random import shuffle

from banco_base_2 import Jogador, Propriedade
from comportamentos import Comportamentos


def cria_jogadores():
    jogadores = []
    for x in range (1, 5):
        jogadores.append(Jogador(f'Jogador {x}'))

    shuffle(jogadores)

    return jogadores


def cria_propriedades():
    propriedades = []

    for x in range(1, 21):
        propriedades.append(Propriedade(f'Propriedade {x}', x))

    return propriedades


def sequencia_acoes(jogador, jogadores, propriedades):
    if jogador.em_jogo:
        jogador.joga_dado()
        jogador.recebe_bonus()
        jogador.atualizar_posicao()
        jogador.pagar_aluguel(propriedades[jogador.posicao_tabuleiro - 1],
                              jogadores)
        comprar = Comportamentos(propriedades[jogador.posicao_tabuleiro -1],
                                 jogador)
        jogador.comprar_propriedade(propriedades[jogador.posicao_tabuleiro -1],
                                    comprar.seleciona_comportamento())
        jogador.monitor_saldo(propriedades)