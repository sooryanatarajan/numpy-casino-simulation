import numpy as np

active_players=np.array([True]*1000)

players_balance=np.full(1000,1000.0)
rounds=60
players=1000
minimum_balance=500
minbet=50


roulette_colors = np.array([
    0,  
    1, 2, 1, 2, 1, 2, 1, 2, 1, 2,  
    2, 1, 2, 1, 2, 1, 2, 1,         
    1, 2, 1, 2, 1, 2, 1, 2,         
    2, 1, 2, 1, 2, 1, 2, 1, 2, 1    
])

slot_symbols = np.arange(6)

slot_emojis = np.array([
    "🍒",
    "🍋",
    "🔔",
    "⭐",
    "💎",
    "👑"
])


slot_probabilities = [
    0.35,
    0.25,
    0.18,
    0.12,
    0.08,
    0.02
]