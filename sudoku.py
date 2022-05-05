#Connor McDougall
#I AM THE KING OF SUDOKU
#Challenge Complete, works on anysize board
# A3, Part 1  


#------------------------------------------------------------------#
# provided function - do NOT remove or change
import math


def load_puzzle(filename):
    ''' Reads a sudoku puzzle from the text file 'filename' in the current directory. 
        Returns a list of lists of integers that represents the game.
            load_puzzle(filename:str) -> str[str[int]]
        Empty cells in the game are denoted by 0s in the file (and the output list)
    '''
    puzzle = [] 
    with open(filename, "r") as f:
        for line in f:
            puzzle.append( [int(val) for val in line.split(",")] )
    return puzzle


# Prints the sudoku puzzle in a barely readable manner
#  sudoku boards come in standard 4x4,6x6,8x8 and 9x9, but mine works on (almost) Any!

def puzzle_to_string(list: [int]):
    z = 0
    C = 0
    R = 0
    L = len(list)
    global SudokuNumber
    SudokuNumber = len(list)
   
    C = SimFactors(L)
    R = int(L/C)
    
    Max = 2
    for e in list:
        for PAIN in e:
            if (PAIN) > Max:
                Max = (PAIN)
    
    for x in list:
        
        if z != 0 and z % R == 0:
            Store = ""
            for e in Hold:
                if e == "|": 
                    Store += "+"
                else:
                    Store += "-"
            print(Store)
        Hold = ""
        for i in range(0,L):
            if i != 0 and i % C == 0:
                Variable = str(x[i])
                if Variable == "0":
                    Variable = " "
                Hold += "|" + " " +Variable  + " "
            elif str(x[i]) == "0":
                
                Hold += "  "
            else:
               
                Hold += str(x[i]) + " "
        print(Hold)
        z += 1
#------------------------------------------------------------------#
#------------------------------------------------------------------#

#Check the horizontal rows

def check_rows(list : [[int]], zeroCheck : bool = False) -> [int]:
    Re = []
    for x in range(0,len(list)):
        if OnetoNum(list[x],SudokuNumber,zeroCheck) == False:
            Re.append(x)
    return Re


#Check the colums, WHICH IS THE NUMBERS ALIGNED DOWNWARDS, NOT ACROSS

def check_columns(list : [[int]]) -> [int]:
    Re = []
    Send = []
    for x in range(SudokuNumber):
        Send = []
        for i in range(SudokuNumber):
            Send.append(list[i][x])
        if OnetoNum(Send,SudokuNumber) == False:
            Re.append(x)
    return Re


#Checks the Subgrids of the sudoku game

def check_subgrids(list : [[int]]) -> [int]:
    Re = []
    Send = []
    C = SimFactors(SudokuNumber)
    R = int(SudokuNumber/C)

    e = 0
    for q in range(int(SudokuNumber/C)):
        for t in range(int(SudokuNumber/R)):
            #t =t *3
            Send = []
            x = q*C
            y = t*R

            for i in range(SudokuNumber):

               
                Send.append(list[y][x])

                if x != 0 and x == C-1+(q*C):
                    
                    y += 1
                    x = q*C
                else:
                    x += 1
            #print(Send)
            if OnetoNum(Send,SudokuNumber) == False:
                Re.append(e)    
            e += 1
    return Re


# My extra Helper Function
# Checks that no # is outside the range 1-9, and checks for doubles 
# There is some obsolete code in it, but it works, so im too lazy and scared to change it

def OnetoNum(P : [int],Num : int = 9, zeroCheck : bool = False) -> bool:
    
    if len(P) > 9:
        print(P,'too long')
        return False

    s = ""
    for x in P:
        s += str(x)

    for r in s:
        r = int(r)
        if r > SudokuNumber:
            return False

    for x in range(1,(Num+1)):
        e = str(x)
        if zeroCheck == True:
            if s.find('0') >= 0: 
                return False
        if s.find(e,s.find(e,0)+1) < 0:
            continue

        return False    
    return True
#------------------------------------------------------------------#
#------------------------------------------------------------------#

def SimFactors(x : int):
    Diff = 100
    LowX = 1
    for i in range(1, x+1):
        if x % i != 0:
            continue
        e = x / i 
        if abs(e-i) < Diff:
            Diff = abs(e-i)
            LowX = e
    return int(LowX)


#------------------------------------------------------------------#
# Your "program" is driven by the main method
# Modify as needed to test your functions
def main():

    puzzle = load_puzzle('puzzle6.csv')
    puzzle_to_string(puzzle)
    print(check_rows(puzzle))
    print(check_columns(puzzle))
    print(check_subgrids(puzzle))



#------------------------------------------------------------------#
# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()



    '''
    
def puzzle_to_string(list: [int]):
    z = 0
    for x in list:
        Hold = ""
        if z == 3 or z == 6:
            E = "-"*5
            print("", E, "+", E, "+",E)
        for i in range(0,9):
            if i == 3 or i == 6:   
                Hold +=  " " + "|" + " " +str(x[i])
            elif str(x[i]) == "0":
                 Hold += "  "
            else:
                Hold += " " + str(x[i])
        print(Hold)
        z += 1
        '''