from random import randint
lg=randint(1,100)
print("The rules of the game are:\n-If a player's guess is less than 1 or greater than 100,they will have to enter another guess after the message 'OUT OF BOUNDS'\n-On a player's first turn, if their guess is:\n\t-within 10 of the number, the game will return the message 'WARM!'\n\t-further than 10 away from the number,'COLD!'\n\t-If its not within a range of 10 they will see the message 'Nowhere close!'\n-On all subsequent turns, if a guess is\n\t-closer to the number than the previous guess its 'WARMER!'\n\t-farther from the number than the previous guess,its 'COLDER!'\n-When the player's guess equals the number, it tells them they've guessed correctly and how many guesses it took!")
count=1
inp=int(input('Enter no.: '))
while inp!=lg:
   if inp<1 or inp>100:
    inp=int(input('Invalid Input:'))
   else:
    if count==1:
        predif=abs(inp-lg)
        count+=1
        if inp in range(lg-10,lg):
            inp=int(input('WARM!'))
        elif inp in range(lg,lg+10):
            inp=int(input('COLD'))
        else:
            inp=int(input('Nowhere close!'))
    else:
        count+=1
        if abs(inp-lg)<predif:
            predif=abs(inp-lg)
            inp=int(input('WARMER!'))
        elif abs(inp-lg)>predif:
            predif=abs(inp-lg)
            inp=int(input('COLDER!'))
print(f'It took {count} attempts to figure out the number')
