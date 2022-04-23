import sys 

class board():
    def __init__(self):
        self.point = "_"
        self.chars = ["X", "O"]

        self.rows = 6
        self.collumns = 7

        self.rows_for_win = 4 

        self.board = [list(self.point * self.collumns) for row in range(self.rows)]


    def printboard(self):
        b = '\n'
        for i in range(self.rows):
            b += ' '.join(self.board[i]) + '\n'
        print(b)
        for i in range(self.collumns):
            ind = str(i)
            print(ind, end= " ")

    
class move(board):
    def __init__(self):
        super().__init__()
        

    def outofrange(self, row, index):
        try:
            if index >= 0 and index <= len(self.board):
                self.board[row][index]
                return False 
            else:
                return True 
        except IndexError:
            return True 


    def checkwin(self, row, move, player):
        if self.checkwin_up(row, move, player) or self.checkwin_right(row, move, player) or self.checkwin_left(row, move, player) or self.checkwin_down(row, move, player) or self.checkwin_upleft(row, move, player) or self.checkwin_upright(row, move, player) or self.checkwin_downleft(row, move, player) or self.checkwin_downright(row, move, player):
            return True 


    def checkwin_up(self, row, move, player):
        count = 0
        for i in range(self.rows_for_win - 1):
            row -= 1 
            if self.outofrange(row, move):
                break
            else:
                if self.board[row][move] == self.chars[player]:
                    count += 1 

        if count >= 3:
            return True 


    def checkwin_down(self, row, move, player):
        count = 0
        for i in range(self.rows_for_win - 1):
            row += 1
            if self.outofrange(row, move):
                break
            else:
                if self.board[row][move] == self.chars[player]:
                    count += 1

        if count >= 3:
            return True 
         

    def checkwin_right(self, row, move, player):
        count = 0
        for i in range(self.rows_for_win - 1):
            move += 1
            if self.outofrange(row, move):
                break 
            else:
                if self.board[row][move] == self.chars[player]:
                    count += 1
        
        if count >= 3:
            return True 
                

    def checkwin_left(self, row, move, player):
        count = 0
        for i in range(self.rows_for_win - 1):
            move -= 1
            if self.outofrange(row, move):
                break 
            else:
                if self.board[row][move] == self.chars[player]:
                    count += 1

            if count >= 3:
                return True 


    def checkwin_upleft(self, row, move, player):
        count = 0
        for i in range(self.rows_for_win - 1):
            row -= 1
            move -= 1
            if self.outofrange(row, move):
                break
            else:
                if self.board[row][move] == self.chars[player]:
                    count += 1

        if count >= 3:
            return True 

    def checkwin_upright(self, row, move, player):
        count = 0
        for i in range(self.rows_for_win - 1):
            row -= 1
            move += 1
            if self.outofrange(row, move):
                break
            else:
                if self.board[row][move] == self.chars[player]:
                    count += 1

        if count >= 3:
            return True 

    def checkwin_downright(self, row, move, player):
        count = 0
        for i in range(self.rows_for_win - 1):
            row += 1
            move += 1
            if self.outofrange(row, move):
                break
            else:
                if self.board[row][move] == self.chars[player]:
                    count += 1

        if count >= 3:
            return True 

    def checkwin_downleft(self, row, move, player):
        count = 0
        for i in range(self.rows_for_win - 1):
            row += 1
            move -= 1
            if self.outofrange(row, move):
                break
            else:
                if self.board[row][move] == self.chars[player]:
                    count += 1

        if count >= 3:
            return True 


    def makeMove(self, player):
        move = int(input("Choose Collumn: "))
        for i in reversed(range(self.rows)):
            if self.board[i][move] == "_":  # Changing position by indexing into the list 
                self.board[i][move] = self.chars[player]
                if self.checkwin(i, move, player):
                    return True     
                break
            if i == 0:
                print("Collumn is full, choose another!")
                self.makeMove(player)


class game(move):
    def __init__(self):
        super().__init__()

    def start(self):
        gameon = True 
        while gameon:
            print("\n\nX's turn")
            if self.makeMove(0):
                print(f"{self.chars[0]} wins!")
                gameon = False 
                self.printboard()   
                sys.exit()
            else:
                self.printboard()   

            print("\n\nO's Turn") 

            if self.makeMove(1):
                print(f"{self.chars[1]} wins!")
                gameon = False 
                self.printboard() 
                sys.exit()
            else:
                self.printboard()   
