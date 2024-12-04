
# adding global variabels

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board 
def printBoard(board):
  print(board[0] + "|" + board[1] + "|" + board[2])
  print("_____")
  print(board[3] + "|" + board[4] + "|" + board[5])
  print("_____")
  print(board[6] + "|" + board[7] + "|" + board[8])
printBoard(board)  
  
# take player input 
def playerInput(board):
  inp = int(input("Enter a number between 1-9 : "))
#check if the input is between 1-9 by using the if statement
  if inp >= 1 and inp <= 9 and board[inp-1] == "-":
     board[inp-1] = currentPlayer 
  else:
    print(" player is already in that spot! ")
    
    
    
# check for win or tie 
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
      winner = board[0]
      return True
      
    elif board[3] == board[4] == board[5] and board[3] != "-":
      winner = board[3]
      return True 
      
    elif board[6] == board[7] == board[8] and board[6] != "-":
      winner = board[6]
      return True 
      
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
      winner = board[0]
      return True
      
    elif board[1] == board[4] == board[7] and board[1] != "-":
      winner = board[1]
      return True
      
    elif board[2] == board[5] == board[8] and board[2] != "-":
      winner = board[2]
      return True
      
    
def checkDiag(board):
  global winner
  if board[0] == board[4] == board[8] and board[0] != "-":
      winner = board[0]
      return True
          
  elif board[2] == board[4] == board[6] and board[2] != "-":
      winner = board[2]
      return True     
      
def checkTie(board):
  global gameRunning
  if "-"  not in board:
    printBoard(board)
    print("it's a Tie!")
    gameRunning = False
    
    
def checkWin():
    global winner
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
      printBoard(board)
      print(f"the winner is {winner}")  
      exit()            
      
      
# switch the player  
def switchPlayer():
  global currentPlayer
  if currentPlayer == "X":
    currentPlayer = "O"
  else:
    currentPlayer = "X"
    
           
    
while gameRunning:
  printBoard(board)
  playerInput(board)    
  checkWin()
  checkTie(board)
  switchPlayer()
  checkWin()
  checkTie(board)          
  
  