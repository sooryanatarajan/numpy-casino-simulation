
import numpy as np

import config
def display_stats_round(roundno, player_bets, player_balance, player_status,died):
    print("=================================================================")
    print()
    print("Round: ", roundno)
    print("Maximum bet: ", player_bets.max())
    print("Smallest bet", player_bets.min())
    print("Maximum balance: ", player_balance.max())
    print("Minimum balance: ", player_balance.min())
    print("Active players: ", player_status.sum())
    print("Average bet: ", player_bets[player_status].mean())
    print("Players eliminated this round: ", died)
    print()


def display_stats_final(player_balance,player_status,player_behaviour,dead,overallalive):
    print()
    print()
    print("=================================================================")
    print("Players left: ", overallalive)
    print("Players dead: ", dead)
    print()
    print("Total money left: ", player_balance.sum())
    print("Maximum balance: ", player_balance.max())
    print("Average balance: ", player_balance.mean())
    print("Lowest balance: ", player_balance.min())
