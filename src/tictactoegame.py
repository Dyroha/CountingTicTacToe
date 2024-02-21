from random import randint

#a class representing a tic-tac-toe game with useful utility methods
class TicTacToe:
    LINES = [[(0,0),(1,1),(2,2)],
             [(0,1),(1,1),(2,1)],
             [(0,2),(1,1),(2,0)],
             [(1,0),(1,1),(1,2)],
             [(0,0),(0,1),(0,2)],
             [(0,2),(1,2),(2,2)],
             [(2,0),(2,1),(2,2)],
             [(0,0),(1,0),(2,0)],
            ]
    
    def __init__(self):
        self.board = [[" "," "," "] for _ in range(3)]
        self.turn = 0
        self.gameOver = False
        self.pieceOrder = []
    
    def __str__(self) -> str:
        temp = [" " + "|".join(x) for x in self.board]
        return "\n-------\n".join(temp)
    
    def placePiece(self, y, x):
        if self.validMove(y,x):
            self.turn += 1
            piece = "X" if self.turn % 2 == 1 else "O"
            self.board[y][x] = piece
            self.pieceOrder.append((y,x))
            if self.checkWin():
                print(self)
                print(f'{piece} Wins!!!')
                self.gameOver = True
            elif self.turn >= 9:
                self.gameOver = True
                print(self)
                print("Game was a draw")
        else:
            print("Invalid move")
            print(y,x)
            print(self)
            
    def validMove(self, y, x):
        return self.board[y][x] == " ";
            
    def checkWin(self):
        for line in self.LINES:
            l = [self.board[y][x] for (y,x) in line]
            if l.count(l[0]) == 3  and l[0] != " ":
                return True

                

if __name__ == "__main__":
    ttt = TicTacToe()
    y = randint(0,2)
    x = randint(0,2)
    
    count = 0
    while not ttt.gameOver and count < 100:
        if not ttt.validMove(y,x):
            y = randint(0,2)
            x = randint(0,2)
            count += 1
        else:
            count = 0
            ttt.placePiece(y,x)
            
    if count >= 100:
        print(ttt)
    print(ttt.pieceOrder)