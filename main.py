#rock paper scissors
import random is rd

def usr_input():
    usr = input("Choose one! ROCK(r), PAPER(p), SCISSORS(s): ")
    match usr.lower():
        case "r":
            usr = 0
        case "p":
            usr = 1
        case "s":
            usr = 2
    return usr

def comp_input():
    comp = rd.randint(0,2)
    return comp

def who_won(usr, comp):
    usr_wins = 0
    comp_wins = 0

    if usr == 0:
        if comp == 0:
            None
        elif comp == 1:
            comp_wins += 1
        elif comp == 2:
            usr_wins += 1
    elif usr == 1:
        if comp == 0:
            usr_wins += 1
        elif comp == 1:
            None
        elif comp == 2:
            comp_wins += 1
    elif usr == 2:
        if comp == 0:
            comp_wins += 1
        elif comp == 1:
            usr_wins += 1
        elif comp == 2:
            None
    return (usr_wins, comp_wins)

def game():
    num_of_rounds = int(input("How many rounds do you want to play?"))

    for rounds in range(num_of_rounds):       
        usr = usr_input()
        comp = comp_input()
        who_won(usr, comp)
        



