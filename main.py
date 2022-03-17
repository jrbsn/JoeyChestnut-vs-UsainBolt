import numpy as np
# average fit male 20-30 100m time: 16s

chestnutDashTime = [18,25] # estimated
chestnutDogTime = 5.62

usainDashTime = 9.58
usainDogTime = [12,23] #estimated

sims = 100000
chestnutWins = 0
usainWins = 0
draws = 0
for sim in range(sims):
    cDash = np.random.randint(chestnutDashTime[0] * 100, chestnutDashTime[1] * 100) / 100
    uDog = np.random.randint(usainDogTime[0] * 100, usainDogTime[1] * 100) / 100

    cTime = cDash + chestnutDogTime
    uTime = uDog + usainDashTime

    if cTime > uTime:
        usainWins += 1
    elif cTime == uTime:
        draws += 1
    else:
        chestnutWins += 1

print("Chestut Wins: %i" % chestnutWins)
print("Bolt Wins: %i" % usainWins)
print("Draws: %i" % draws)