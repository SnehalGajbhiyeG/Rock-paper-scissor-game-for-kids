import random
def gamewin(comp, you) :
    if comp == you :
        return None 
    
    elif comp == 'rock' :
        if you == 'paper' :
            return False
        elif you == 'scissor' :
            return True 

    elif comp == 'scissor' :
        if you == 'rock' :
            return False
        elif you == 'paper' :
            return True

    elif comp == 'paper' :
        if you == 'scissor' :
            return False 
        if you == 'rock' :
            return True 

print('Comp Turn: rock, paper or scissor') 
randNo = random.randint(1, 3)
if randNo == 1 :
    comp = 'rock'
elif randNo == 2 :
    comp = 'paper' 
elif randNo == 3 :
    comp = 'scissor'

you = input('Your Turn: rock, paper or scissor: ')     
a = gamewin(comp, you) 

print(f'Computer choose {comp}') 
print(f'You choose {you}') 

if a == None :
    print("The game is tie") 
elif a :
    print("You win !") 
else:
    print('You lose') 