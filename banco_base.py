from random import randint


class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.em_jogo = True
        self.saldo = 300
        self.posicao_tabuleiro = 0
        self.classificacao_final = None

    def joga_dado(self):
        self.posicao_tabuleiro += (randint(1,6))

    def recebe_bonus(self):
        if self.posicao_tabuleiro > 20:
            self.saldo += 100

    def atualizar_posicao(self):
        if self.posicao_tabuleiro > 20:
            self.posicao_tabuleiro -= 20

    def pagar_aluguel(self, propriedade, jogadores):

        if propriedade.dono_propriedade:
            self.saldo -= propriedade.valor_aluguel

            for jogador in jogadores:
                if jogador.nome == propriedade.dono_propriedade:
                    jogador.saldo += propriedade.valor_aluguel

    def comprar_propriedade(self, propriedade, comprar):
        if self.saldo > propriedade.valor_venda \
                and not propriedade.dono_propriedade\
                and comprar:
            propriedade.dono_propriedade= self.nome
            self.saldo -= propriedade.valor_venda

    def monitor_saldo(self, propriedades):
        if self.saldo <= 0:
            self.em_jogo = False
            self.devolve_propriedades(propriedades)

    def devolve_propriedades(self, propriedades):
        for propriedade in propriedades:
            if propriedade.dono_propriedade == self.nome:
                propriedade.dono_propriedade = None


def classificacao(jogadores):
    ganhador = sorted(jogadores, key=lambda k: (k.saldo), reverse=True)[0]
    return f'O {ganhador.nome} foi o ganhador com um saldo de {ganhador.saldo}.'


def encerra_jogo(jogadores):
    jogadores_ativos = list(filter(lambda x: x.em_jogo == True, jogadores))
    if len(jogadores_ativos) == 1:
        return True


class Propriedade:

    VALOR_VENDA = [58, 51, 60, 56, 53, 87, 81, 81, 88,
                   84, 99, 94, 92, 108, 105, 118, 121,
                   110, 128, 130]

    def __init__(self, nome, posicao, lista_valor = VALOR_VENDA):
        self.nome_propriedade = nome
        self.posicao_tabuleiro = posicao
        self.valor_venda = lista_valor[posicao - 1]
        self.valor_aluguel = self.valor_venda * 0.5
        self.dono_propriedade = None





















