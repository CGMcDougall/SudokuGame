#Connor McDougall

#Sudoku Game
#Works for any size board, not just (n^2)x(n^2)
# Maybe more bonus marks for it working on any board...? ....maybe.... ...please... 


import sudoku

#The Intro code that only needs to happen once
#asks for which puzzle to load in
#Options are puzzle1, puzzle2 and puzzle6 rn

def Intro():
    print("Welcome to Sudoku Game!")
    while True:
        try:
            P = input("Please input a Sudoku Puzzle : ")
            P = f'SudokuPuzzles/{P}.csv'
            p = sudoku.load_puzzle(P)
            break
        except Exception as e:
            print(e)
            continue
    return p


# A function that calls all the "Checks" from my sudoku program
# takes a potial board state, and returns that same board state if it is valid, otherwise it retuns [0]

def ValidCheck(List : [[int]], Row : int, Col : int, Num : int):
    Temp = List.copy()
    Hold  = Temp[Col][Row]
    Temp[Col][Row] = Num

    
    if len(sudoku.check_columns(Temp) + sudoku.check_rows(Temp) + sudoku.check_subgrids(Temp)) <= 0:
        return Temp
    # I dont know why, but i have to add this for it to work, if i dont, the temp value num replaces its counterpart in puzzle
    Temp[Col][Row] = Hold

    return [0]




#The Engine in the program
#aka has a while loop that drives the repetition part of the program

def Engine(puzzle : [[int]]):

    #The "Useful" info about the game variables
    Engine.Tried = 0
    Engine.Failed = 0
    Engine.Victory = False


    while True:
        sudoku.puzzle_to_string(puzzle)
        E = input("(Format: ROW;COL;NUMBER) : ")

        #quit game option
        if E.lower() == "quit":
            print("Bye")
            break

        Engine.Tried += 1
        #formats the input
        C = E.split(";")

        #sends the potetial board state
        
        Temp = ValidCheck(puzzle,int(C[0]),int(C[1]),int(C[2]))
    
        #checks to see if board state is valid
        if Temp == [0]:
            print("Invalid Entry")
            input("Press Enter to continue")
            Engine.Failed += 1
            
            continue
        
        
        puzzle = Temp

        #checks to see if you won by seeing if there is any 0s left
        if sudoku.check_rows(puzzle,True) == []: 
            Engine.Victory = True
            break

     
# My god tear main funtion
#as in tears from crying
#i didnt misspell it

def main():
    puzzle = Intro()
    Engine(puzzle)
    if Engine.Victory == True:
        print("Congrats, you won")
    else:
        print("You Lost")
    print("You entered", Engine.Tried, "numbers.")
    print("You entered an incorect number", Engine.Failed, "times")



# Main where my main function runs from

if __name__ == "__main__":
    main()

