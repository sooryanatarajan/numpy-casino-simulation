import numpy as np
import config
rng=np.random.default_rng()
def coin_toss(player_balance, player_status, player_bets):
    toss=rng.integers(0,2)
    guesses=np.zeros_like(player_balance)
    guesses[player_status]=rng.integers(0,2,player_status.sum())
    outcome = np.zeros_like(player_status, dtype=bool)
    outcome[player_status] = guesses[player_status] == toss
    losses=player_status & ~outcome
    player_balance[outcome]+=(player_bets[outcome])
    player_balance[losses] -= (player_bets[losses])
    condition = player_balance > config.minimum_balance
    player_status[condition]=True
    player_status[~condition]=False

