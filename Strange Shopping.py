## Strange Shopping ##

## Import files, modules, libraries

import time
import random

## Functions and variables

def display_menu():

    ## prepare the main menu

    main_menu = {
        1: "Start Game",
        2: "Read Instructions",
        3: "Exit Program"
    }

    ## display the main menu
    print("<-----STRANGE SHOPPING----->")
    for i in main_menu:
        print(f'{i} : {main_menu[i]}')
    
    ## ask for user input.
    time.sleep(1)
    print("What do you want to do today?")
    menu_choice = int(input("> "))
    if menu_choice == 1:
        start_game()
    elif menu_choice == 2:
        show_instructions()
    elif menu_choice == 3:
        return
    else:
        print("Please provide a valid response.")
        time.sleep(1)
        display_menu()

def show_instructions():

    time.sleep(1)
    print("<-----SHOW INSTRUCTIONS----->")
    print("The store is doing an auction!")
    print("You need to outbid the rest of the bidders buy getting as many items as you can.")

    time.sleep(2)
    print("<-----ROUND FLOW----->")
    print("Each round is composed of BIDDING > SHOWDOWN > CONCLUSION")

    time.sleep(2)
    print("<-----BIDDING----->")
    print("At the start of each round, the game will show the item for bidding.")
    print("You'll also be shown your cash cards.")
    print("You'll use these cash cards to bid.")
    print("You can input as many cash cards as you desire.")
    print("Once you're okay with your bid, input 'DONE'")
    
    time.sleep(2)
    print("<-----SHOWDOWN----->")
    print("After the bidding round, your bid will be compared to the bids of other people.")
    print("Whoever gets the highest total bid will win the item.")
    print("Your goal is to get as many items as possible while saving money.")

    display_menu()

def start_game():

    time.sleep(1)
    print("<-----GAME START----->")

    ## declare global variables.
    global player_score,player_cards,opponent_cards,opponent_score, round_counter

    ## initialize player variables
    player_score = 0
    player_cards = [1,2,3,4,5,6,7,8,9]

    ## initialize opponent variables
    opponent_score = 0
    opponent_cards = [1,2,3,4,5,6,7,8,9]
    
    round_counter = 1

    round_start()

def round_start():

    ## declare global variables.
    global player_score,player_cards,opponent_cards,opponent_score, round_counter

    ## start the game.
    print(f'<-----ROUND {round_counter}----->')
    print(f'Player Score : {player_score}')
    print(f'Opponent Score : {opponent_score}')
    
    time.sleep(1)

    ## display the cards

    card_tray = ""
    print("Choose one of your cards: ")
    for card in player_cards:
        card_tray = card_tray + " " + str(card)
        
    print(card_tray)

    global player_choice,opponent_choice

    player_choice = int(input("> "))

    if player_choice not in player_cards:
        print("That amount is not available to you.")
        round_start()

    opponent_choice = opponent_cards[random.randint(0,len(opponent_cards))]
    showdown()

def showdown():
    global player_choice, opponent_choice
    global player_score,player_cards,opponent_cards,opponent_score, round_counter

    print(f'You used {player_choice}')

    print(f'Bidder A used {opponent_choice}')

    time.sleep(1)
    if player_choice > opponent_choice:
        print("You won!")
        player_cards.remove(player_choice)
        opponent_cards.remove(opponent_choice)

        player_score += 1
        round_counter += 1
        round_start()
    elif player_choice < opponent_choice:
        print("The opponent won!")
        player_cards.remove(player_choice)
        opponent_cards.remove(opponent_choice)

        opponent_score += 1
        round_counter += 1
        round_start()
    elif player_choice == opponent_choice:

        print("All bidders used the same amount of cash.")
        print("No card have been used.")

    
## WORKFLOW 

display_menu()




    