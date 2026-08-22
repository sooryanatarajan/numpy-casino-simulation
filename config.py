import numpy as np

active_players=np.array([True]*1000)

players_balance=np.full(1000,1000.0)
rounds=50
players=1000
minimum_balance=500
minbet=50


# 0 = Green, 1 = Red, 2 = Black
roulette_colors = np.array([
    0,  # 0
    1, 2, 1, 2, 1, 2, 1, 2, 1, 2,  # 1-10
    2, 1, 2, 1, 2, 1, 2, 1,         # 11-18
    1, 2, 1, 2, 1, 2, 1, 2,         # 19-26
    2, 1, 2, 1, 2, 1, 2, 1, 2, 1    # 27-36
])
