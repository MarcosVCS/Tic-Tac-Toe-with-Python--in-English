# SELECT PLAYER
def player_assign():
    
    print("\nFirst player, choose your side!")

    player1_symbol = ''
    while player1_symbol not in ['O', 'o', 'X', 'x']:
        player1_symbol = input("Do you want to play as X or O? ")

        if player1_symbol not in ['O', 'o', 'X', 'x']:
            print("First player, please choose either 'X' or 'O'!")
    
    if player1_symbol.upper() == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# BOARD
import os

def board_structure(V1,V2,V3,V4,V5,V6,V7,V8,V9):
    try:
        os.system('cls')     # Para usuários Windows
    except:
        os.system('clear')   # Para usuários Linux/ OS X

    print("+---+---+---+")
    print(f"  {V1} | {V2} | {V3}")
    print("+---+---+---+")
    print(f"  {V4} | {V5} | {V6}")
    print("+---+---+---+")
    print(f"  {V7} | {V8} | {V9}")
    print("+---+---+---+")

# PLAYS
def player_choice(player):
    play = 0
    while play < 1 or play > 9:
        print(f'\nPlayer {player}, choose where do you want to play!')
        play = int(input('Choice: '))

        if play < 1 or play > 9:
            print('Invalid command!')
            print("Let's try it again! \n")

    return (play)

# GAME (MAIN FUNCTIONS WILL BE CALLED HERE)
def game():
    # FIRST PLAYER CHOOSES HIS SYMBOL
    player1_symbol, player2_symbol = player_assign()
    
    # INITIAL BOARD VARIABLES (THEY WILL BE MODIFIED DURING THE GAME)

    pos = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}

    # INITIAL BOARD
    board_structure(pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],pos[9])

    contador = 0
    while contador < 9: #LIMITS THE NUMBER OF PLAYS (CHECKS TIES)

        # FIRST PLAYER MOVES

        play = player_choice('1')
        while pos[play] == 'X' or pos[play] == 'O':    #ERRO AQUI - REFAZER ESSA LÓGICA (RELAÇÃO COM LINHA 55)/ DEPOIS COPIAR 2o PLAYER
            print('\nThis place has already been chosen!\nPlease pick another...')
            play = player_choice('1')
        else:
            pos[play] = player1_symbol
            contador += 1

        # FIRST PLAYER WINNING CONDITIONS
        if (pos[1] == pos[2] == pos[3]) or (pos[4] == pos[5] == pos[6]) or (pos[7] == pos[8] == pos[9]) or (pos[1] == pos[4] == pos[7]) or (pos[2] == pos[5] == pos[8]) or (pos[3] == pos[6] == pos[9]) or (pos[1] == pos[5] == pos[9]) or (pos[3] == pos[5] == pos[7]):
            board_structure(pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],pos[9])
            print('\nVitória do Player 1!')
            break

        # BOARD MODIFIED AFTER FIRST PLAYER MOVES
        board_structure(pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],pos[9])

        # SECOND PLAYER MOVES
        play = player_choice('2')
        while pos[play] == 'X' or pos[play] == 'O':
            print('\nThis place has already been chosen!\n Please pick another...')
            play = player_choice('2')
        else:
            pos[play] = player2_symbol
            contador += 1

        # SECOND PLAYER WINNING CONDITIONS
        if (pos[1] == pos[2] == pos[3]) or (pos[4] == pos[5] == pos[6]) or (pos[7] == pos[8] == pos[9]) or (pos[1] == pos[4] == pos[7]) or (pos[2] == pos[5] == pos[8]) or (pos[3] == pos[6] == pos[9]) or (pos[1] == pos[5] == pos[9]) or (pos[3] == pos[5] == pos[7]):
            board_structure(pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],pos[9])
            print('\nVitória do Player 2!')
            break

        # BOARD MODIFIED AFTER SECOND PLAYER MOVES
        board_structure(pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8],pos[9])
    else: 
        print('Empate!')

# WELCOME MESSAGE
print("\nWELCOME TO TIC-TAC-TOE!")

# ONGOING GAME
newgame = True 
while newgame == True:

    game() # CALL NO JOGO

    # REPLAY
    ans_newgame = ""
    while ans_newgame not in ['Y','y','N','n']:
        ans_newgame = input('Do you want to keep playing? (Y/n) ')
        if ans_newgame.upper() == 'Y':
            newgame = True
        else: newgame = False
    else:
        continue

print('Thanks for playing!')

