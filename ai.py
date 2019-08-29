class Ai():
    def __init__(self, stage):
        self.current_target = None
        self.stage = stage
        self.controlled_bases = []
        self.enemy_bases = []
        self.neutral_bases = []
        self.target_base = None
        self.selected_bases = []

        self.i = 0

    def base_inventory(self):
        self.controlled_bases = []
        self.enemy_bases = []
        self.neutral_bases = []
        for base in self.stage.bases:
            if base.team == 'enemy':
                self.controlled_bases.append(base)
            elif base.team == 'neutral':
                self.neutral_bases.append(base)
            else:
                self.enemy_bases.append(base)

    def select_target(self):
        # todo if there are no bases left to pick it creates a list index out of range
        # todo make it prioritize neutrals
        self.target_base = None
        sorted_bases = sorted(self.enemy_bases + self.neutral_bases, key=lambda x: x.inhabitants)
        self.target_base = sorted_bases[0]


    def select_base(self):
        self.selected_bases = []
        for base in self.controlled_bases:
            if base.inhabitants > 20:
                self.selected_bases.append(base)

    def send_creatures(self):
        for base in self.selected_bases:
            if not base.currently_releasing:
                base.transfer_creatures(self.target_base)

    def update(self):
        self.base_inventory()
        self.select_target()
        self.select_base()

        self.i += 1
        if self.i > 60:
            self.send_creatures()
            self.i = 0
