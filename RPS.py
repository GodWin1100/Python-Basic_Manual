import random

CPU=['ROCK','PAPER','SCISSOR']
playcpu=random.choice(CPU)
player=int(input('1=Rock\t2=Paper\t3=Scissor : '))
if(player==1):
    playplayer='ROCK'
elif (player == 2):
    playplayer = 'PAPER'
elif (player == 3):
    playplayer = 'SCISSOR'
else:
    print("Please Select Correct Option...")

print('Player = ',playplayer,' VS ','CPU = ',playcpu)
if(playcpu==playplayer):
    print('Tie')
elif(playcpu=='ROCK' and playplayer=='PAPER'):
    print("Player Wins!!!")
elif (playcpu == 'PAPER' and playplayer == 'SCISSOR'):
    print("Player Wins!!!")
elif (playcpu == 'SCISSOR' and playplayer == 'ROCK'):
    print("Player Wins!!!")
else:
    print('CPU Wins!!!')