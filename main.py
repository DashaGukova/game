import datetime
import os


# Create new file
class Log:
    name = ""
    file = open("test.txt", "w")
    now = datetime.datetime.now()
    file.write('{}, {}'.format(now.strftime("%d-%m-%Y %H:%M"), name))
    file.close()


# Create Menu
class Menu:
    def __init__(self, ans, file):
        self.ans = ans
        self.file = file

    print('Choose one of the options:')
    print('1 - play')
    print('2 - log')
    print('3 - delete log')
    print('4 - exit')
    ans = input()

# Selecting menu items
    if ans == "1":
        main()
    elif ans == "2":
        Log()
        try:
            file = open("test.txt", "r")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print('Not found')
        except IOError:
            print('Something else')
    elif ans == "3":
        Log()
        os.remove("test.txt")
    else:
        exit()


class Table:  # This class creates tables for visualization and filling
    def __init__(self, board, mainboard):
        self.board = board
        self.mainboard = mainboard

    mainboard = {'7': ' ', '8': ' ', '9': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '1': ' ', '2': ' ', '3': ' '}

    board_keys = []

    for key in mainboard:
        board_keys.append(key)

    def printboard(self):
        print(self.board['7'] + "|" + self.board['8'] + "|" + self.board['9'])
        print('-+-+-')
        print(self.board['4'] + "|" + self.board['5'] + "|" + self.board['6'])
        print('-+-+-')
        print(self.board['1'] + "|" + self.board['2'] + "|" + self.board['3'])

    def __setitem__(self, index, value):
        self.board[index] = value

    def __getitem__(self, index):
        return self.board[index]


# The main function which has all the gameplay functionality.
def main():
    turn = "X"
    count = 0
    print('if you want to play with "X" type your name')
    player1 = input()
    print('if you want to play with "O" type your name')
    player2 = input()

    # For each move the loop calls the table
    for i in range(10):
        h = Table()
        mainboard = h.mainboard
        h.printboard(mainboard)
        print("It's your turn, {}.Move to free place".format(turn))

        move = input()

        # Check free place in the table
        if mainboard[move] == ' ':
            mainboard[move] = turn
            count += 1
        else:
            print('That place is already filled.\nMove to another place?')
            continue

        # Check if player X or O has won,for every move after 5 moves.
        f = Log()
        if count >= 5:
            if mainboard['7'] == mainboard['8'] == mainboard['9'] != ' ':  # Won with top cells
                h = Table()
                mainboard = h.mainboard
                h.printboard(mainboard)
                print('\nGame Over.\n')
                print(' **** {} won. **** '.format(turn))
                if turn == "X":  # Find name of winner
                    f.name = player1
                else:
                    f.name = player2
                break
            elif mainboard['4'] == mainboard['5'] == mainboard['6'] != ' ':  # Won with middle cells
                h = Table()
                mainboard = h.mainboard
                h.printboard(mainboard)
                print('\nGame Over.\n')
                print(' **** {} won. **** '.format(turn))
                if turn == 'X':
                    f.name = player1
                else:
                    f.name = player2
                break
            elif mainboard['1'] == mainboard['2'] == mainboard['3'] != ' ':  # Won with bottom cells
                h = Table()
                mainboard = h.mainboard
                h.printboard(mainboard)
                print('\nGame Over.\n')
                print(' **** {} won. **** '.format(turn))
                if turn == "X":
                    f.name = player1
                else:
                    f.name = player2
                break
            elif mainboard['1'] == mainboard['4'] == mainboard['7'] != ' ':  # Won with left cells
                h = Table()
                mainboard = h.mainboard
                h.printboard(mainboard)
                print('\nGame Over.\n')
                print(' **** {} won. **** '.format(turn))
                if turn == "X":
                    f.name = player1
                else:
                    f.name = player2
                break
            elif mainboard['2'] == mainboard['5'] == mainboard['8'] != ' ':  # Won with middle vertical cells
                h = Table()
                mainboard = h.mainboard
                h.printboard(mainboard)
                print('\nGame Over.\n')
                print(' **** {} won. **** '.format(turn))
                if turn == "X":
                    f.name = player1
                else:
                    f.name = player2
                break
            elif mainboard['3'] == mainboard['6'] == mainboard['9'] != ' ':  # Won with right cells
                h = Table()
                mainboard = h.mainboard
                h.printboard(mainboard)
                print('\nGame Over.\n')
                print(' **** {} won. **** '.format(turn))
                if turn == "X":
                    f.name = player1
                else:
                    f.name = player2
                break
            elif mainboard['7'] == mainboard['5'] == mainboard['3'] != ' ':  # Won with left diagonal cells
                h = Table()
                mainboard = h.mainboard
                h.printboard(mainboard)
                print('\nGame Over.\n')
                print(' **** {} won. **** '.format(turn))
                if turn == "X":
                    f.name = player1
                else:
                    f.name = player2
                break
            elif mainboard['1'] == mainboard['5'] == mainboard['9'] != ' ':  # Won with right diagonal cells
                h = Table()
                mainboard = h.mainboard
                h.printboard(mainboard)
                print('\nGame Over.\n')
                print(' **** {} won. **** '.format(turn))
                if turn == "X":
                    f.name = player1
                else:
                    f.name = player2
                break

                # if nobody won, declare tie
        if count == 9:
            print('\nGame Over.\n')
            print("It's a Tie!!")
            f.name = "Tie"

        # Change the player after every move.
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

            # Ask players want to restart the game or not.
    restart = input('Do you want to play Again?(yes/no)')
    d = Table()
    keys = d.board_keys
    boards = d.mainboard
    if restart == "yes" or restart == "Yes":
        for key in keys:
            boards[key] = " "

        main()


if __name__ == "__main__":
    main()
