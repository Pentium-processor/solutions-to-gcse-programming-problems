import random 
import time
dice_numbers=list(range(1,7,1))
player_1_score=[]
player_2_score=[]
count=0
def create_winner_file():
    
    with open("winners.txt","a") as a: 
      a.write("Winners:\n") 
      if sum(player_1_score)>sum(player_2_score):
         a.write(f'\t{count}. player 1:{player_1_username}')
      else:
         a.write(f'\t{count}. player 2:{player_2_username}')

player_1_username=input('player 1 username:')
time.sleep(1)
player_2_username=input('player 2 username:')
def player_1_turn():
    
    roll_first_dice=input("Press enter to roll the first dice:")
    print('Player 1 rolls the first dice.')
    time.sleep(0.01)
    print(first_dice)
    time.sleep(0.01)
    roll_second_dice=input("Press enter to roll the second dice:")
    print('PLayer 1 rolls the second dice.')
    time.sleep(0.01)
    print(second_dice)
    time.sleep(0.01)
    if total%2==0:
        player_1_score.append(total+10)
    else:
        player_1_score.append(total-5)
def player_2_turn():
    roll_first_dice=input("Press enter to roll the first dice:")
    print('Player 2 rolls the first dice.')
    time.sleep(0.01)
    print(first_dice)
    time.sleep(0.01)
    roll_second_dice=input("Press enter to roll the second dice:")
    print('PLayer 2 rolls the second dice.')
    time.sleep(0.01)
    print(second_dice)
    if total_1%2==0:
        player_2_score.append(total_1+10)
    else:
        player_2_score.append(total_1-5)
for n in range(5):
    first_dice=random.choice(dice_numbers)
    second_dice=random.choice(dice_numbers)
    player_2_first_dice=random.choice(dice_numbers)
    player_2_second_dice=random.choice(dice_numbers)
    total=first_dice+second_dice
    total_1=player_2_first_dice+player_2_second_dice
    player_1_turn()
    player_2_turn()
else:
    print('player 1 score:',sum(player_1_score))
    print('player 2 score:',sum(player_2_score))
    if sum(player_1_score)>sum(player_2_score):
        print('Player 1 wins!')
    elif sum(player_2_score)>sum(player_1_score):
        print('Player 2 wins!')
    elif sum(player_2_score)==sum(player_1_score):
        random_dice=random.choice(['first dice','second dice'])
        roll_last_die=input(f"press enter to roll your last dice {player_1_username}:")
        print('Player 1 rolls the ',random_dice)
        if random_dice=='first dice':
            player_1_score.append(first_dice)
        elif random_dice=='second dice':
            player_1_score.append(second_dice)
        time.sleep(1)
        roll_last_die=input(f"press enter to roll your last dice {player_2_username}:")
        print('Player 2 rolls the ',random_dice)
        if random_dice=='first dice':
            player_2_score.append(player_2_first_dice)
        elif random_dice=='second dice':
            player_2_score.append(player_2_second_dice)
        time.sleep(1)
        print('player 1 score:',sum(player_1_score))
        print('player 2 score:',sum(player_2_score))
        if sum(player_1_score)>sum(player_2_score):
         print(f'{player_1_username} wins!')
        elif sum(player_2_score)>sum(player_1_score):
         print(f'{player_2_username} wins!')
        
create_winner_file()