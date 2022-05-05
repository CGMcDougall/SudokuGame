Author: Connor McDougall
Program: Sodoku Game
Purpose: Play a game of sudoku in the terminal of with a board of any size!

Launch: py puzzle.py

Operation:
	
	On initilaziation, yoy will be prompted to enter a "puzzle"	
		Document type must be a .csv and must be in the "SudokuPuzzles" folder
		If incorrect puzzle is inputed, you will be propted until valid puzzle is inputted
		Board can be of any size or dimension, even one not typically alowed
	
	After the puzzle has loaded, it will be printed in to the terminal
		From here, you can input a answer into a slot
			Follow format Row;Col;Num (ex: 1;1;4)
		If the input is invalid (as in breaks the rules of sudoku) it will be refused
		Otherwise, the number will be put into the slot
	
	If the puzzle has been completed, it will print a congratulation into the terminal

	
Files:
	
	SudokuPuzzles/puzzle1
	SudokuPuzzles/puzzle2
	SudokuPuzzles/puzzle6
	puzzle.py
	README.txt
	sudoku.py