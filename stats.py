
import numpy as np

import config
def display_stats_round(roundno, player_bets, player_balance, player_status):
    print("=================================================================")
    print()
    print("Round: ", roundno)
    print("Maximum bet: ", player_bets.max())
    print("Smallest bet", player_bets.min())
    print("Maximum balance: ", player_balance.max())
    print("Minimum balance: ", player_balance.min())
    print("Active players: ", player_status.sum())
    print()
    

