import numpy as np
import games
import config
import stats
rng=np.random.default_rng()


player_status=config.active_players
player_balance=config.players_balance

def run_simulation():
    for i in range(config.rounds):
        active_balances = player_balance[player_status]
        player_bet=np.zeros_like(player_balance)
        player_bet[player_status]=rng.integers(config.minbet, active_balances+1)
        games.coin_toss(player_balance, player_status, player_bet)
        stats.display_stats_round(i,player_bet,player_balance,player_status)
        
