from time import sleep
import random


def new_line():
    """
    -> Add a little pause between the textes
    :return: an empty line for organization
    """
    sleep(0.8)
    print()


def game():
    """
    -> Main game is made here
    :return: who won the game
    """

    pc_choice = player_choice = player_num = ''

    pc_num = random.randint(1, 3)
    # I can use the word the number represent chosen with this if, elif. In both cases, for pc and the player
    if pc_num == 1:
        pc_choice = 'PAPER'
    elif pc_num == 2:
        pc_choice = 'SCIZOR'
    elif pc_num == 3:
        pc_choice = 'ROCK'

    if player_num == '1':
        player_choice = 'PAPER'
    elif player_num == '2':
        player_choice = 'SCIZOR'
    elif player_num == '3':
        player_choice = 'ROCK'

    sleep(0.8)
    # While so the user can't digit anything else that it is meant for
    # "not in 1 or 2 or 3" - So the user cant bug typing '12' in player_num
    while player_num not in '1' or '2' or '3':
        player_num = str(input('==========================================================='
                               '\n1 - Paper'
                               '\n2 - Scizor'
                               '\n3 - Rock'
                               '\nWhat number you choice: ')).strip()
        if player_num == '':
            game()

        # Game situations
        if pc_num == 1 and player_num == '1' or pc_num == 2 and player_num == '2' or pc_num == 3 and player_num == '3':
            print(f'{player_choice}'.center(60))
            new_line()
            print(f'PC chose {pc_choice}'.center(60))
            print('DRAW'.center(60))
            game()
        if pc_num == 1 and player_num == '2' or pc_num == 2 and player_num == '3' or pc_num == 3 and player_num == '1':
            print(f'{player_choice}'.center(60))
            new_line()
            print(f'PC chose {pc_choice}'.center(60))
            print(f'\'{player_name}\' WINS'.center(60))
            sleep(0.8)
            print('CONGRATULATIONS'.center(60))
            print('===========================================================')
            retry()
        if pc_num == 1 and player_num == '3' or pc_num == 2 and player_num == '1' or pc_num == 3 and player_num == '2':
            print(f'{player_choice}'.center(60))
            new_line()
            print(f'PC chose {pc_choice}'.center(60))
            print('PC WINS'.center(60))
            sleep(0.8)
            print('GAME OVER'.center(60))
            print('===========================================================')
            retry()


def retry():
    """
    -> Restart the game
    :return: the user's input
    """
    # while so the user cant digit anything else that is meant for
    # not in 'y' or 'n' - So the user cant bug typing 'yn' or any word that starts with 'y' or 'n'
    try_again = ''
    while try_again not in 'y' or 'n':
        try_again = str(input('Want to retry? [y/n] ')).strip().lower()
        if try_again == '':
            try_again = str(input('Want to retry? [y/n] ')).strip().lower()
        if try_again == 'y':
            game()
        if try_again == 'n':
            exit()


new_line()
player_name = str(input('Your playing name: ')).strip()
