#Implementation of Two Player Tic-Tac-toe inPython
theboard = {'7':' ', '8':' ','9':' ',
            '4':' ','5':' ','6':'',
            '1':' ','2':' ','3':' '}
board_keys = []
for key in theboard:
    board_keys.append(key)
def printBoard(board):
    print(board[7]+'|'+board['8']+'|'+board['9'])
    print('-+-+-')
    print(board[4]+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board[1]+'|'+board['2']+'|'+board['3'])
def game():
    turn ="x"
    count = 0
    for i in range(10):
        printBoard[theboard]
        print("it's your turn"+ turn+",move to which place?")
        move = input()
        if theboard[move] ==' ':
            theboard[move] = turn
            count+= 1
        else:
            print("that place is already filled./nMove to whichplace?")
            continue
        if count>= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] !=' ':
                printBoard(printBoard)
                print("/nGame Over./n")
                print("****"+turn+"won. ****")
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] !=' ':
                printBoard(printBoard)
                print("/nGame Over./n")
                print("****"+turn+"won. ****")
                break
            elif theboard['1'] == theboard['2'] == theboard['3'] !=' ':
                printBoard(printBoard)
                print("/nGame Over./n")
                print("****"+turn+"won. ****")
                break
            elif theboard['1'] == theboard['4'] == theboard['7'] !=' ':
                printBoard(printBoard)
                print("/nGame Over./n")
                print("****"+turn+"won. ****")
                break
            elif theboard['2'] == theboard['5'] == theboard['8'] !=' ':
                printBoard(printBoard)
                print("/nGame Over./n")
                print("****"+turn+"won. ****")
                break
            elif theboard['3'] == theboard['6'] == theboard['9'] !=' ':
                printBoard(printBoard)
                print("/nGame Over./n")
                print("****"+turn+"won. ****")
                break
            if count == 9:
                print("/nGame Over")
                print("it's a tie!!")
                if turn =="x":
                    turn = "o"
                else:
                    turn ="X"
                    restart = input("do u want to play again?(y/n)")
                    if restart == "y" or restart == "Y":
                        for key in board_keys:
                            theboard[key]=" "
                            game()
                            game()