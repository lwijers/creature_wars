import base
import pygame

class Level_mngr():
    def __init__(self, stage):
        self.levels = levels
        self.stage = stage

    def give_lvl(self, lvl):
        constructed_level = []
        x = 0
        y = 0
        inhabitants = 0
        for team in self.levels[lvl]['bases']:
            team = team
            for amount in range(self.levels[lvl]['bases'][team]['amount']):
                try:
                    x = self.levels[lvl]['bases'][team]['stats'][amount][0]
                    y = self.levels[lvl]['bases'][team]['stats'][amount][1]
                    inhabitants = self.levels[lvl]['bases'][team]['stats'][amount][2]
                    constructed_level.append(base.Base(self.stage, x, y, team, inhabitants))
                except IndexError:
                    print('Whoops you specified a number of enemies but didnt give them stats')
                    pygame.quit()
        return constructed_level


levels = {
    '1': {
        'bases' : {
            'enemy' : {
                'amount' : 1,
                'stats' : [
                    [100, 400, 400],
                ]
            },
            'neutral' : {
                'amount' : 2,
                'stats' : [
                    [400, 400, 20],
                    [60, 200, 10]
                ]
            },
            'player' : {
                'amount' : 2,
                'stats' : [
                    [300, 600, 30],
                    [400, 600, 30]
                ]
            }
        }
    }
}





# number of enemy bases
# number of player bases
# number of neutral bases
# location of bases
# inhabitants per base

# eventually:
# upgrades of enemy
# level image


