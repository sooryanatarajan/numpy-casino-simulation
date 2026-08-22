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
    player_balance[outcome] += np.floor(player_bets[outcome] * 0.95).astype(int)
    player_balance[losses] -= (player_bets[losses])
    condition = player_balance > config.minimum_balance
    player_status[condition]=True
    player_status[~condition]=False


    
def roulette(player_balance, player_status, player_bets, player_behaviour):
    # bet_type 
    # 0  Red/Black
    # 1  Even/Odd
    # 2  Dozen
    # 3  Single Number
    cmask=player_status & (player_behaviour==0)
    nmask=player_status & (player_behaviour==1)
    rmask=player_status & (player_behaviour==2)
    bet_type=np.zeros_like(player_balance)
    player_guess=np.zeros_like(player_balance)
    conv=np.array([0,1])
    normie=np.array([1,2])
    risky=np.array([2,3])
    bet_type[cmask] = rng.choice(conv,size=cmask.sum())
    bet_type[nmask] = rng.choice(normie,size=nmask.sum())
    bet_type[rmask] = rng.choice(risky,size=rmask.sum())

    #setup red/black game, 0 for red, 1 for black
    rbmask=bet_type==0
    player_guess[rbmask]=rng.integers(1,3,rbmask.sum())

    #setup even/odd game, 0 for even, 1 for odd
    eomask=bet_type==1
    player_guess[eomask]=rng.integers(0,2,eomask.sum())

    #setup dozen game
    dmask=bet_type==2
    guesses=[0,1,2]
    player_guess[dmask]=rng.choice(guesses,size=dmask.sum())

    #setup single number game
    smask=bet_type==3
    player_guess[smask]=rng.integers(0,37,smask.sum())

    #setup outcomes
    # 0 = Green, 1 = Red, 2 = Black

    rollnumber=rng.integers(0,37)
    eo=(7 if rollnumber==0 else rollnumber%2 )
    rollcolour=config.roulette_colors[rollnumber]
    outcome=np.zeros_like(player_status,dtype=bool)
    rdozen=-1
    if 1<=rollnumber<=12:
        rdozen=0
    elif 13<=rollnumber<=24:
        rdozen=1
    elif 25<=rollnumber<=36:
        rdozen=2

    #r/b game
    outcome[rbmask]= player_guess[rbmask] == rollcolour

    #even/odd game

    outcome[eomask] = player_guess[eomask] == eo

    #dozen game

    outcome[dmask] = player_guess[dmask] == rdozen

    #single number

    outcome[smask] = player_guess[smask] == rollnumber
    losses=player_status & ~outcome
    player_balance[losses]-=player_bets[losses]
    player_balance[outcome & rbmask] += player_bets[outcome & rbmask]
    player_balance[outcome & eomask] += player_bets[outcome & eomask]
    player_balance[outcome & dmask] += player_bets[outcome & dmask]*2
    player_balance[outcome & smask] += player_bets[outcome & smask]*35
    condition = player_balance > config.minimum_balance
    player_status[condition]=True
    player_status[~condition]=False








    


