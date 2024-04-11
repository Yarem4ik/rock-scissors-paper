import random

def get_user_choice():
    user_choice = input("Обери камінь (k), ножиці (n) або папір (p): ")
    return user_choice.lower()

def get_computer_choice():
    choices = ['k', 'n', 'p']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Нічия!"
    elif (user_choice == 'k' and computer_choice == 'n') or \
         (user_choice == 'n' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'k'):
        return "Ти виграв(ла)!"
    else:
        return "Ти програв(ла)!"

def play_game():
    print("Гра 'Камінь, ножиці, папір'!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Твій вибір: {user_choice}")
    print(f"Вибір комп'ютера: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()
