def main():
    difficulty = input("Difficult or Casual? ")
    players = input ("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend ("poker")
        elif players == "Single-player":
            recommend ("klondike")
        else:
            print("Enter a valid number of players")
    elif difficulty == "Casual":
            if players == "Multiplayer":
                 recommend("Hearts")
            else:
                 recommend("Clock")
    else:
            print("Enter a valid difficulty")
            

def recommend(game):
    print("You might like", game)

main()
