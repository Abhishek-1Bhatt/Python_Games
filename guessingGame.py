count=0
guess=0
inp=int(input('Enter your guess: '))
pre=inp
while inp!=lg:
    if count==0:
        if inp<= lg+10 and inp>=lg-10:
            print('Warm!')
        else:
            print('Cold!')
        count = count+1
        continue
    count=count+1
    inp=int(input('Guess Again :) '))
    if inp==lg:
        print(f'Hey! you guessed it right after {count} attempts')
    elif inp>lg and pre>lg:
        if inp-lg<pre-lg:
            print('Warmer!')
        elif inp-lg>pre-lg:
            print('Colder!')
    elif inp<lg and pre<lg:
        if lg-pre>lg-inp:
            print('Warmer!')
        elif lg-pre<lg-inp:
            print('Colder!')
if count==0:
    print('Congrats, guessed it right in the first attempt!')
