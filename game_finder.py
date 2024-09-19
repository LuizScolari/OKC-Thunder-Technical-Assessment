"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""

from collections import defaultdict
from datetime import datetime

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
    # Dictionary to store players grouped by gameID
    games = defaultdict(list)

    # Group players by gameID
    for player_data in game_data:
        games[player_data['gameID']].append(player_data)
    
    qualified_games = []

    # Process each gameID only once
    for gameID, players in games.items():
        total_player_count = 0

        # Count how many players have a TS% greater than or equal to the cutoff
        for player in players:
            fieldGoal2Attempted = player['fieldGoal2Attempted']
            fieldGoal2Made = player['fieldGoal2Made']
            fieldGoal3Attempted = player['fieldGoal3Attempted']
            fieldGoal3Made = player['fieldGoal3Made']
            freeThrowAttempted = player['freeThrowAttempted']
            freeThrowMade = player['freeThrowMade']
            
            # Calculate total attempts considering 2P, 3P, and free throws (adjusted by 0.44)
            total_attempts = fieldGoal2Attempted + fieldGoal3Attempted + 0.44 * freeThrowAttempted
            if total_attempts > 0:  # Avoid division by zero
                true_shooting = ((2 * fieldGoal2Made + 3 * fieldGoal3Made + freeThrowMade) / 
                                 (2 * total_attempts)) * 100
                if true_shooting >= true_shooting_cutoff:
                    total_player_count += 1

        # Check if the number of qualified players meets the required player_count
        if total_player_count >= player_count:
            # Add the gameID and game date to the list of qualified games
            gameDate = players[0]['gameDate']  # The date is the same for all players in the same game
            qualified_games.append((gameID, gameDate))

    # Sort the games by date (from most recent to oldest)
    qualified_games.sort(key=lambda x: datetime.strptime(x[1], '%m/%d/%Y'), reverse=True)

    # Return only the gameIDs in the correct order
    return [game[0] for game in qualified_games]