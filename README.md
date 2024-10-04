# OKC Thunder Technical Assessment - Internship Test

## Description

This project was developed as part of the technical assessment for the **Oklahoma City Thunder** internship program. The goal was to implement the `find_qualified_games` function in the `game_finder.py` file, which filters and returns a list of games where a minimum number of players met or exceeded a given True Shooting Percentage (TS%).

### Task Requirements

The `find_qualified_games` function accepts the following parameters:

1. **game_data**: A list of dictionaries where each dictionary represents a player's shot attempts in a game. Each dictionary contains the following keys:
   - `gameID` (int): Unique identifier for the game.
   - `playerID` (int): Unique identifier for the player.
   - `gameDate` (str): Date of the game in the format 'MM/DD/YYYY'.
   - `fieldGoal2Attempted` (int): Number of two-point field goals attempted.
   - `fieldGoal2Made` (int): Number of two-point field goals made.
   - `fieldGoal3Attempted` (int): Number of three-point field goals attempted.
   - `fieldGoal3Made` (int): Number of three-point field goals made.
   - `freeThrowAttempted` (int): Number of free throws attempted.
   - `freeThrowMade` (int): Number of free throws made.

2. **true_shooting_cutoff**: The minimum True Shooting percentage required for a player to qualify in a game. It will be an integer value ≥ 0.

3. **player_count**: The number of players who need to meet or exceed the `true_shooting_cutoff` for a game to be considered qualified. It will be an integer value ≥ 0.

### Objective

The `find_qualified_games` function should return a list of unique `gameID`s where at least `player_count` players achieved a True Shooting percentage greater than or equal to the `true_shooting_cutoff`, ordered from the most recent game to the least recent.

### Sample Test Cases

Some test cases are provided in the `tests` folder, but additional test cases may be used for evaluation.
