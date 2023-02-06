import random
import json

# # Traditional Bingo: balls are numbered from 1 to 75 and the board is labeled BINGO
bingo_letters = ['B', 'I', 'N', 'G', 'O']
balls = range(1,76)import random
import json

# # Traditional Bingo: balls are numbered from 1 to 75 and the board is labeled BINGO
bingo_letters = ['B', 'I', 'N', 'G', 'O']
balls = range(1,76)

# # Music Trivia Bingo. The length of the balls should be divisible by the length of the bingo letters.
# balls = ['Foo Fighters', 'Guns N Roses', 'Rock3', 'Rock4', 'Rock5',
#          'Reba', 'Dolly Parton', 'Country3', 'Country4', 'Country5',
#          'Nirvana', 'Pearl Jam', 'Grunge3', 'Grunge4', 'Grunge5',
#          'Michael Jackson', 'Madonna', 'Pop3', 'Pop4', 'Pop5',
#          'Tracy Chapman', 'Ke$ha', 'PowerWomen3', 'PowerWomen4', 'PowerWomen5',]
# bingo_letters = ['Rock', 'Country', 'Grunge', 'Pop', 'PowerWomen']

# Sanity check
if len(balls)%len(bingo_letters) != 0:
    print('The number number of classes needs to divide the number of balls.')
    quit()

class Cell:
    def __init__(self, value: str, id: int, row: int, col: int) -> None:
        self.value = value
        self.id = id
        self.row = row
        self.col = col

def make_bingo_board():
    # Create an even dispersion of the balls into the letters
    number_association = { }
    board_length = len(bingo_letters)
    number_of_balls = len(balls)
    for i in range(board_length):
        letter_range = []
        for j in range( i*(number_of_balls//board_length),  (i+1)*(number_of_balls//board_length) ):
            letter_range.append(balls[j])
        number_association[bingo_letters[i]] = letter_range
    # print(number_association)

    board = []
    if board_length%2 != 0:
        for i in range(board_length):
            if i == board_length//2:
                board.append(random.sample(number_association[bingo_letters[i]], k=board_length//2)+['Free Space']+random.sample(number_association[bingo_letters[i]], k=board_length//2))
            else:
                board.append(random.sample(number_association[bingo_letters[i]], k=board_length))
    else:
        for i in range(len(bingo_letters)):
            board.append(random.sample(number_association[bingo_letters[i]], k=len(bingo_letters)))
        
    ret_board = []
    for i in range(len(board)):
        ret_board.append([board[j][i] for j in range(len(board))])
        
    return ret_board
        
def make_json_board(bingo_board):
    # Create JSON file for the board
    JSONboard = []
    idNo = 0
    for i in range(len(bingo_board)):
        for j in range(len(bingo_board)):
            JSONboard.append(Cell(bingo_board[j][i],idNo,i,j,))
            idNo += 1
            
    jsonStr = json.dumps([ob.__dict__ for ob in JSONboard], indent=2)

    jsonFile = open("test_bingo_board.json", "w")
    jsonFile.write(jsonStr)
    jsonFile.close()
    
    return jsonStr

random_board = make_bingo_board()

for i in random_board:
    print(i)

print('')

print(make_json_board(random_board))

# # Music Trivia Bingo. The length of the balls should be divisible by the length of the bingo letters.
# balls = ['Foo Fighters', 'Guns N Roses', 'Rock3', 'Rock4', 'Rock5',
#          'Reba', 'Dolly Parton', 'Country3', 'Country4', 'Country5',
#          'Nirvana', 'Pearl Jam', 'Grunge3', 'Grunge4', 'Grunge5',
#          'Michael Jackson', 'Madonna', 'Pop3', 'Pop4', 'Pop5',
#          'Tracy Chapman', 'Ke$ha', 'PowerWomen3', 'PowerWomen4', 'PowerWomen5',]
# bingo_letters = ['Rock', 'Country', 'Grunge', 'Pop', 'PowerWomen']

if len(balls)%len(bingo_letters) != 0:
    print('The number number of classes needs to divide the number of balls.')
    quit()

# Create an even dispersion of the balls into the letters
number_association = { }
board_length = len(bingo_letters)
number_of_balls = len(balls)
for i in range(board_length):
    letter_range = []
    for j in range( i*(number_of_balls//board_length),  (i+1)*(number_of_balls//board_length) ):
        letter_range.append(balls[j])
    number_association[bingo_letters[i]] = letter_range
# print(number_association)

board = []
if board_length%2 != 0:
    for i in range(board_length):
        if i == board_length//2:
            board.append(random.sample(number_association[bingo_letters[i]], k=board_length//2)+['Free Space']+random.sample(number_association[bingo_letters[i]], k=board_length//2))
        else:
            board.append(random.sample(number_association[bingo_letters[i]], k=board_length))
else:
    for i in range(len(bingo_letters)):
        board.append(random.sample(number_association[bingo_letters[i]], k=len(bingo_letters)))
    
for i in range(len(board)):
    print([board[j][i] for j in range(len(board))])
    
class Cell:
    def __init__(self, value: str, id: int, row: int, col: int) -> None:
        self.value = value
        self.id = id
        self.row = row
        self.col = col
        
# Create JSON file for the board
JSONboard = []
idNo = 0
for i in range(len(board)):
    for j in range(len(board)):
        JSONboard.append(Cell(board[j][i],idNo,i,j,))
        idNo += 1
        
jsonStr = json.dumps([ob.__dict__ for ob in JSONboard], indent=2)

jsonFile = open("test_bingo_board.json", "w")
jsonFile.write(jsonStr)
jsonFile.close()