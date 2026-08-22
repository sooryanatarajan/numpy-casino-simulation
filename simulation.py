import numpy as np
import games
import config
import stats
import time
rng=np.random.default_rng()

player_number=np.arange(config.players)

player_status=config.active_players

player_balance=config.players_balance

player_taken=np.zeros_like(player_balance,dtype=bool)

choose_conservative=rng.choice(player_number, size=300, replace=False)

player_behaviour=np.full(config.players,2)

player_behaviour[choose_conservative]=0

player_taken[choose_conservative]=True

available=player_number[~player_taken]

choose_moderate=rng.choice(available,size=300,replace=False)

player_behaviour[choose_moderate]=1

player_taken[choose_moderate]=True

def run_simulation():
    beforeoverall=player_status.sum()
    for i in range(config.rounds):
        choice=rng.integers(0,2)
        old=player_balance.copy()
        player_bet=np.zeros_like(player_balance)
        cmask= (player_status) & (player_behaviour==0)
        rmask= (player_status) & (player_behaviour==2)
        nmask= (player_status) & (player_behaviour==1)
        high = np.maximum(
    (player_balance[cmask] * 0.1).astype(int),
    config.minbet

)
        player_bet[cmask]=rng.integers(config.minbet, high+1)

        high = np.maximum(
    (player_balance[nmask] * 0.3).astype(int),
    config.minbet
)
        player_bet[nmask]=rng.integers(config.minbet, high+1)

        high = np.maximum(
    (player_balance[rmask] * 0.5).astype(int),
    config.minbet
)
        player_bet[rmask]=rng.integers(config.minbet,high+1)

        before=player_status.sum()
        if choice==0:
            games.coin_toss(player_balance, player_status, player_bet)
            gamename= "COIN TOSS"
        elif choice==1:
            games.roulette(player_balance,player_status,player_bet,player_behaviour)
            gamename= "ROULETTE"


        after=player_status.sum()
        new=player_balance.copy()
        profit=old-new
        
        stats.display_stats_round(i+1,player_bet,player_balance,player_status, before-after,profit,gamename)
        time.sleep(1)
    overallalive=player_status.sum()
    dead=beforeoverall-overallalive
    stats.display_stats_final(player_balance,player_status,player_behaviour,dead,overallalive)