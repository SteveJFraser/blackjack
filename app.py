from random import choice

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

intro = "Do you want to play a game of Blackjack? Type 'y' or 'n': "

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards_list = []
computer_cards_list = []


def clear_screen():
    print("\n"*50, flush=True)


def print_logo():
    print(logo)


def deal_cards():
    player_card1 = choice(cards)
    player_card2 = choice(cards)
    computer_card1 = choice(cards)
    computer_card2 = choice(cards)

    player_cards_list.append(player_card1)
    player_cards_list.append(player_card2)

    computer_cards_list.append(computer_card1)
    computer_cards_list.append(computer_card2)
    print_logo()
    b = "\b"*4
    return f"""\nYour cards: : {player_cards_list}, current score: {sum(player_cards_list)}
    {b}Computer's first card: {computer_cards_list[0]}"""
    

def get_another_card():
    add_card = choice(cards)
    player_cards_list.append(add_card)


def add_player_cards():
    return sum(player_cards_list)    


def add_computer_cards():
    return sum(computer_cards_list)


def final_checking():
    if add_player_cards() < add_computer_cards() <= 21:
        print_logo()
        print(f"You lose 😤, Computer score: {add_computer_cards()}, "
              f"Your score: {add_player_cards()}")
        print()
    elif add_player_cards() > 21:
        print_logo()
        print(f"You lose 😤, Computer score: {add_computer_cards()}, "
              f"Your score: {add_player_cards()}")
        print()
    elif add_computer_cards() == 21 and add_player_cards() < 21:
        print_logo()
        print(f"You lose 😤, Computer score: {add_computer_cards()}, "
              f"Your score: {add_player_cards()}")
        print()
    elif add_computer_cards() > 21 >= add_player_cards():
        print_logo()
        print(f"You win! 🥳🤩😁 yay, Computer score: {add_computer_cards()}, "
              f"Your score: {add_player_cards()}")
        print()
    elif add_computer_cards() < add_player_cards() <= 21:
        print_logo()
        print(f"You win! 🥳🤩😁 yay, Computer score: {add_computer_cards()}, "
              f"Your score: {add_player_cards()}")
        print()
    elif add_player_cards() == 21 and add_computer_cards() < 21:
        print_logo()
        print(f"You win! 🥳🤩😁 yay, Computer score: {add_computer_cards()}, "
              f"Your score: {add_player_cards()}")
        print()
    elif add_computer_cards() == add_player_cards():
        print_logo()
        print(f"Tie!, your final score: {sum(player_cards_list)},"
              f" computer score: {sum(computer_cards_list)}")
        print()


clear_screen()
print_logo()
while (user_input := input(intro)) != "n".lower():
    player_cards_list.clear()
    computer_cards_list.clear()
    if user_input.casefold() == "y":
        clear_screen()
        print(deal_cards())
        print()
        prompt_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if prompt_another_card.casefold() == "y":
            clear_screen()
            get_another_card()
            final_checking()
        elif prompt_another_card.casefold() == "n":
            clear_screen()
            final_checking()
