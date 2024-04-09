import random


def gerar_board(linhas, colunas, bombas):
  board = [['0' for _ in range(colunas)] for _ in range(linhas)]

  
  bombas_colocadas = 0
  while bombas_colocadas < bombas:
    linha = random.randint(0, linhas - 1)
    coluna = random.randint(0, colunas - 1)

    if board[linha][coluna] != '*':
      board[linha][coluna] = '*'
      bombas_colocadas += 1

      
      for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
          if 0 <= i < linhas and 0 <= j < colunas and board[i][j] != '*':
            board[i][j] = str(int(board[i][j]) + 1)

  return board


def exibir_board(board):
  for linha in board:
    print(' '.join(linha))


def jogar():
  linhas = int(input("Digite a quantidade de linhas do tabuleiro: "))
  colunas = int(input("Digite a quantidade de colunas do tabuleiro: "))
  bombas = int(input("Digite a quantidade de bombas: "))

  board = gerar_board(linhas, colunas, bombas)
  board_revelado = [['-' for _ in range(colunas)] for _ in range(linhas)]

  while True:
    exibir_board(board_revelado)
    linha = int(input("Digite a linha que deseja apresentar: "))
    coluna = int(input("Digite a coluna que deseja apresentar: "))

    if board[linha][coluna] == '*':
      print("Game over,tente novamente")
      exibir_board(board)
      break
    else:
      board_revelado[linha][coluna] = board[linha][coluna]


if __name__ == "__main__":
  jogar()
