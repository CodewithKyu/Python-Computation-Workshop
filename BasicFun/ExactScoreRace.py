#ExactScoreRace is a turn-based dice game where 4 players compete to be the first to reach exactly 100 points. Players take turns rolling a standard 6-sided die, and the sum of their rolls must equal exactly 100 to win. If a roll would cause a player's score to exceed 100, their turn is skipped.

import random

# Initialise scores for 4 players
scores = [0, 0, 0, 0]
current_player = 0
target = 100

print("Ludo Game - First to 100 wins!")

while True:
    # Roll dice
    dice = random.randint(1, 6)
    print(f"\n Player {current_player + 1} rolled: {dice}")
    
    # Update score
    new_score = scores[current_player] + dice
    
    if new_score == target:
        scores[current_player] = new_score
        print(f"Player {current_player + 1} WINS!")
        break
    elif new_score < target:
        scores[current_player] = new_score
        print(f"Player {current_player + 1} score: {new_score}")
    else:
        print(f"Player {current_player + 1} cannot move (would exceed 100)")
    
    # Show all scores
    print("Current scores:", scores)
    
    # Move to next player
    current_player = (current_player + 1) % 4

print("\nFinal scores:", scores)
