from copy import deepcopy

class Spell():
    def __repr__(self):
        return str(self.timer)
    def __init__(self, cost, timer, mana, dmg, arm, heal):
        self.cost = cost
        self.maxTime = timer
        self.timer = -1
        self.mana = mana
        self.dmg = dmg
        self.heal = heal
        self.arm = arm
    def applyEffect(self, player, boss):
        player['hp'] += self.heal
        player['mana'] += self.mana
        boss['hp'] -= self.dmg
        self.timer -= 1

spells = {
        "Magic Missile":Spell(53, 1, 0, 4, 0, 0 ),
        "Drain":Spell(73, 1, 0, 2, 0, 2 ),
        "Shield":Spell(113, 6, 0, 0, 7, 0 ),
        "Poison":Spell(173, 6, 0, 3, 0, 0 ),
        "Recharge":Spell(229, 5, 101, 0, 0, 0 )
}

player = {'hp':50, 'dmg':0, 'arm':0, 'mana':500}
boss = {'hp':51, 'dmg':9, 'arm':0}
answer = 999999

def findLeast(player, boss, spells, manaUsed, playerTurn):
    if playerTurn:
        player['hp'] -= 1
    
    global answer
    for key in spells:
        if key == "Shield":
            if spells[key].timer <= 0:
                player['arm'] = 0
            else:
                player['arm'] = spells[key].arm

        e = spells[key]
        if e.timer > 0:
            e.applyEffect(player, boss)

    if boss['hp'] <= 0:
        if manaUsed < answer:
            answer = manaUsed
        return

    if player['hp'] <= 0 or manaUsed > answer:
        return

    if playerTurn:
        for key in spells:
            p=player.copy()
            if p['mana'] >= spells[key].cost and spells[key].timer <= 0:
                cost = spells[key].cost
                p['mana'] -= cost
                cp = deepcopy(spells)
                cp[key].timer = cp[key].maxTime
                findLeast(p.copy(), boss.copy(), cp, manaUsed + cost, not playerTurn)
    else:
        bossDMG = max(boss['dmg'] - player['arm'], 1)
        player['hp'] -= bossDMG
        findLeast(player.copy(), boss.copy(), spells, manaUsed, not playerTurn)


findLeast(player, boss.copy(), spells, 0, True)


print(answer)