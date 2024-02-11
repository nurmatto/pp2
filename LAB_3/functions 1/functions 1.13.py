import random

print('Hello! What\'s your name?')
your_name = input()
print()
print(f'Well, {your_name}, I am thinking of a number between 1 and 20.')
print('Take a guess.')

value = random.randint(1, 20)
cnt = 0  
while True:
    your_guess = int(input())
    cnt += 1 
    if your_guess < value:
        print('Your guess is too low.')
        print('Take a guess.')
    elif your_guess > value:
        print('Your guess is too high.')
        print('Take a guess.')
    else:  
        print(f'Good job, {your_name}! You guessed my number in {cnt} guesses!')
        break  # Exit the loop

    print() 