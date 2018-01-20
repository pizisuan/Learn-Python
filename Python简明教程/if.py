number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # new block begin
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # new block end
elif guess < number:
    # another block begin
    print('No, it is a a little higher than that')
    # you can do whatever things in this code block
else:
    print('No, it is a little lower than that')
    # you should be guess a little bigger number to get this way
print('Done')
# last statement
