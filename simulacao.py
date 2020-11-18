from banco_simulacao import cria_jogadores, cria_propriedades, sequencia_acoes
from banco_base_2 import classificacao, encerra_jogo


jogadores = cria_jogadores()
propriedades = cria_propriedades()


for x in range(1000):
    for jogador in jogadores:
        sequencia_acoes(jogador, jogadores, propriedades)
        jogadores_ativos = encerra_jogo(jogadores)
        if jogadores_ativos:
            break

    if jogadores_ativos:
        break


for jogador in jogadores:
    print(jogador.nome, jogador.saldo)

ganhador = classificacao(jogadores)
print(ganhador)



