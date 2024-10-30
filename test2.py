import time
import random
import os

os.system("cls")

def print_tabuleiro(tabuleiro):
    """Exibe o tabuleiro em seu estado atual."""
    for linha in tabuleiro:
        print(" ".join(map(str, linha)))
    print("\n")

# Configurações do jogo
tamanho = 9  # Dimensão do tabuleiro
quantidade_obstaculos = int(input("Digite um numero de obstaculos entre 0 a 99: "))
while quantidade_obstaculos < 0:
    print("Valor negativo nao permitido, coloque um numero positivo ou 0!")
    quantidade_obstaculos = int(input("\nDigite um numero de obstaculos entre 1 a 99: "))


# Inicialização do tabuleiro 9x9
tabuleiro = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

# Posição inicial e final
posicao_inicial = (4, 0)
posicao_final = (4, 8)

# Define obstáculos aleatórios representados por '2', diferentes das posições inicial e final
obstaculos = set()
while len(obstaculos) < quantidade_obstaculos:
    obstaculo = (random.randint(0, tamanho - 1), random.randint(0, tamanho - 1))
    if obstaculo != posicao_inicial and obstaculo != posicao_final:
        obstaculos.add(obstaculo)

# Marca os obstáculos no tabuleiro
for ox, oy in obstaculos:
    tabuleiro[ox][oy] = 2

# Função para verificar se a posição é válida e sem obstáculos '2'
def posicao_valida(nx, ny):
    return 0 <= nx < tamanho and 0 <= ny < tamanho and tabuleiro[nx][ny] != 2 and tabuleiro[nx][ny] != 1

# Função de cálculo da distância Manhattan
def distancia(posicao_atual, destino):
    return abs(posicao_atual[0] - destino[0]) + abs(posicao_atual[1] - destino[1])

# Posição inicial do jogador
x, y = posicao_inicial
tabuleiro[x][y] = 1  # Marca a posição inicial
caminho = [(x, y)]  # Pilha para rastrear o caminho percorrido

# Exibe o tabuleiro inicial
print("\nTabuleiro inicial:\n")
print_tabuleiro(tabuleiro)
print("*"*100 + "\n")
time.sleep(1)

# Loop de movimentação até o jogador chegar à posição final
while (x, y) != posicao_final:
    movimento_feito = False

    # Avalia os movimentos com base na proximidade ao objetivo
    movimentos = sorted([(dx, dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]],
                        key=lambda m: distancia((x + m[0], y + m[1]), posicao_final))

    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if posicao_valida(nx, ny):
            # Marca a posição atual como parte do caminho e move o jogador
            x, y = nx, ny
            tabuleiro[x][y] = 1  # Marca o caminho percorrido como 1
            caminho.append((x, y))  # Adiciona a posição à pilha
            movimento_feito = True
            break

    if not movimento_feito:
        # Se não conseguiu se mover, retrocede para a posição anterior
        print("Jogador ficou preso, retrocedendo...")
        if caminho:
            tabuleiro[x][y] = 0  # Reseta a posição atual para 0 (limpa o caminho)
            x, y = caminho.pop()  # Volta uma posição na pilha

    # Exibe o tabuleiro atualizado
    print_tabuleiro(tabuleiro)
    time.sleep(0.5)
    print("-"*60)
    
# Exibe o resultado final
if (x, y) == posicao_final:
    print("Objetivo alcançado!")
else:
    print("O jogador ficou preso e não conseguiu chegar ao objetivo.")
