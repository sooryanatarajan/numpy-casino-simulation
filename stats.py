
import numpy as np
#conservative 300 moderate 300 risky 400
import config
def display_stats_round(roundno, player_bets, player_balance, player_status,died,profit,gamename):
    print("=================================================================")
    print()
    print("Round: ", roundno)
    print()
    print(gamename)
    print()
    print("Maximum profit: ", profit.max())
    print("Minimum profit/loss: ", profit.min())
    print("Total winnings: ", profit[profit>0].sum())
    print("Total losses: ", profit[profit<0].sum())
    print("Average bet: ", player_bets[player_status].mean())
    print("Maximum balance: ", player_balance.max())
    print("Minimum balance: ", player_balance.min())
    print("Active players: ", player_status.sum())
    print("Players eliminated this round: ", died)
    print()



def display_stats_final(player_balance,player_status,player_behaviour,dead,overallalive):
    print()
    print()
    print("=================================================================")
    print()
    print("---------------FINAL REPORT--------------------------------------")
    print()
    print("Players left: ", overallalive)
    print("Players dead: ", dead)
    print()
    print("Total money left: ", player_balance.sum())
    print("Maximum balance: ", player_balance.max())
    print("Average balance: ", player_balance[player_status].mean())
    print("Lowest balance: ", player_balance[player_status].min())
    noc=player_status & (player_behaviour==0)
    nom=player_status & (player_behaviour==1)
    nor=player_status & (player_behaviour==2)
    print("No. of conservative players left: ", noc.sum())
    print("No. of moderate players left: ", nom.sum())
    print("No. of risky players left: ", nor.sum())


