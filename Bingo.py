import random

# # Traditional Bingo: balls are numbered from 1 to 75 and the board is labeled BINGO
balls = range(1,76)
bingo_letters = ['B', 'I', 'N', 'G', 'O']

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
    for j in range( i*(number_of_balls//board_length)+1,  (i+1)*(number_of_balls//board_length)+1 ):
        number_association[balls[j-1]] = bingo_letters[i]
# print(number_association)

# Make a random calling 
call_order = random.sample(balls, k=number_of_balls)

# # If you want to see the whole order, you can comment out one of these.
# print(call_order)
# for i in call_order:
#     print(number_association[i], i)

print('Press any key for the next number or b when someone has bingo')
next_step = input()
numbers_called = []
while (len(call_order) > 0 and next_step != 'b' and next_step != 'B'):
    number = call_order.pop(0)
    column = number_association[number]
    print('Call: ', column, ' - ', number, '\n')
    numbers_called.append(number)
    print('Press any key for the next number or b when someone has bingo')
    next_step = input()
    print(' ')
    if (next_step == 'b' or next_step == 'B'):
        ordered_list = [number_association[i] + ' - ' + str(i) for i in sorted(numbers_called)]
        print(sorted(ordered_list))
        print('Was there indeed a bingo? Y or N.')
        bingo_check = input()
        print('')
        while bingo_check not in ['Y', 'y', 'N', 'n']:
            print('Unknown entry. Does somebody Have Bingo? Please enter Y or N.')
            print(ordered_list)
            bingo_check = input()
        if (bingo_check == 'Y' or bingo_check == 'y'):
            next_step = 'b'
        else:
            next_step = 'n'

if len(call_order) > 0:
    print(ordered_list)
    print('Congratulations!')
else:
    print('All of the numbers have been called. Something must have went awry.')