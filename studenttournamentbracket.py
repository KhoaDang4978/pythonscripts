# This is a complete tournament bracket with multi-round elimination and tiebreaker logic.
print("Welcome to the student tournament bracket")
print("-----------------------------------------")
import random
players = []
losers = []
current_round = []
next_round = []
while True:
    player_name = str(input("Please register player's name (or 'done' to finish): "))
    players.append(player_name)
    if player_name == 'done':
        players.remove("done")
        random.shuffle(players)
        current_round = players
        while len(current_round) > 1:
          next_round = []
          pairs =[]
          print("Results: ")
          for i in range(0, len(current_round), 2):
               x = random.randint(0, 10)
               y = random.randint(0, 10)
               pairs.append((current_round[i], current_round[i + 1]))
               print(f"{current_round[i]} vs {current_round[i + 1]}: {x} - {y}")
               if x > y:
                    winner = (current_round[i])
                    next_round.append(winner)
                    loser = (current_round[i + 1])
                    losers.append(loser)
                    print(f"The winner is {winner}!")
                    print(f"Player {loser} is eliminated!")
               elif x < y:
                    winner = (current_round[i + 1])
                    next_round.append(winner)
                    loser = (current_round[i])
                    losers.append(loser)   
                    print(f"The winner is {winner}!")
                    print(f"Player {loser} is eliminated!")
               else: 
                    winner = random.choice([current_round[i], current_round[i + 1]])
                    if winner == (current_round[i]):
                         next_round.append(winner)
                         loser = (current_round[i + 1])
                         losers.append(loser)
                    else:
                         next_round.append(winner)
                         loser = (current_round[i])
                         losers.append(loser)
                    print("It's a tie! Random tiebreaker!")
                    print(f"The winner is {winner}!")
                    print(f"Player {loser} is eliminated!")
          current_round = next_round
        print(f"Champion: {current_round[0]}!")
        break
