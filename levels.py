import base

class Level_mngr:
    def __init__(self, stage):
        self.levels = levels
        self.stage = stage

    def give_lvl(self, lvl):
        constructed_level = []
        for team in self.levels[lvl]:
            for amount in range(len(self.levels[lvl][team])):
                x = self.levels[lvl][team][amount][0]
                y = self.levels[lvl][team][amount][1]
                inhabitants = self.levels[lvl][team][amount][2]
                constructed_level.append(base.Base(self.stage, x, y, team, inhabitants))
        return constructed_level

levels = {
    "1" : {
        "player" : [
            [300, 600, 30]
        ],
        "neutral" : [
            [400, 400, 20],
            [60, 200, 20],
        ],
        "enemy": [
            [100, 400, 30],
        ]
    }
}
