def battle(player, boss):
    player = player.copy()
    boss = boss.copy()
    while True:
        playerDMG = max(player['dmg'] - boss['arm'], 1)
        boss['hp'] -= playerDMG
        if boss['hp'] <= 0:
            break

        bossDMG = max(boss['dmg'] - player['arm'], 1)
        player['hp'] -= bossDMG

        if player['hp'] <= 0:
            break

    if boss['hp'] > 0:
        return False
    else:
        return True

class Item():
    def __init__(self, cost, dmg ,arm):
        self.cost = cost
        self.dmg = dmg
        self.arm = arm

def buyItem(item, player):
    player['dmg'] += item.dmg
    player['arm'] += item.arm
    return player

weps = [ Item(8,4,0), Item(10,5,0), Item(25,6,0), Item(40,7,0), Item(74,8,0)]
arms = [ Item(13,0,1), Item(31,0,2), Item(53,0,3), Item(75,0,4), Item(102,0,5)]
rings = [ Item(25,1,0), Item(50,2,0), Item(100,3,0), Item(20,0,1), Item(40,0,2), Item(80,0,3) ]

boss = {'hp':103, 'dmg':9, 'arm':2}
player = {'hp':100, 'dmg':0, 'arm':0}

highest = 0
lowest = 9999
for w in range(len(weps)):
    for a in range(len(arms)):
        for r in range(len(rings)):
            for r2 in range(len(rings)):
                player2 = player.copy()
                player2 = buyItem(weps[w], player2)
                player2 = buyItem(arms[a], player2)
                player2 = buyItem(rings[r], player2)
                cost = weps[w].cost + arms[a].cost + rings[r].cost
                if r != r2:
                    cost += rings[r2].cost
                    player2 = buyItem(rings[r2], player2)
                if(battle(player2, boss)):
                    lowest = min(cost, lowest)
                else:
                    highest = max(cost, highest)
    print(lowest)

print("lowest is ",lowest)
print("highest is ", highest)


