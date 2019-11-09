import random
guesses = 0

print(" Hellow ! what's your name ?? \n")
myName = input()

guessnumber =random.randint(1,20)
print('Well ! ' +myName +' I am thinking a number between 1 to 20 lets try to match !!  ')

for guesses in range(6):
    print("Take a guess ")
    guess = input()
    guess =int(guess)
    
    if guess < guessnumber :
        print("Your guess is too low ")
        
    if guess >guessnumber :
        print("your guess is too high !")
        
    if guess == guessnumber :
        break 
if guess == guessnumber :
    guesses = str(guesses + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + 
           guesses + ' guesses!') 
    
if guess != guessnumber :
    
    guessnumber = str(guessnumber)
    print('Nope. The number I was thinking of was ' + guessnumber + '.')
    
        
    
