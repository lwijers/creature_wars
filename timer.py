import pygame

class Timer():
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.time_lapsed = 0
        self.alarms = []

    def set_alarm(self, name, time):
        self.alarms.append(Alarm(name, time))

    def remove_alarm(self, alarm_name):
        for alarm in self.alarms:
            if alarm.name == alarm_name:
                self.alarms.remove(alarm)

    def check_alarm(self, alarm_name):
        for alarm in self.alarms:
            if alarm.flagged:
                if alarm_name == alarm.name:
                    return True
                return False

    def update(self):
        # print('test')
        for alarm in self.alarms:
            alarm.flagged = False
            new_time = pygame.time.get_ticks()
            alarm.current_time = (new_time - alarm.start_time) / 1000
            if alarm.current_time >= alarm.goal_time:
                alarm.flagged = True
                alarm.reset()

        # self.check_alarms()

class Alarm():
    def __init__(self, name, goal_time):
        self.name = name
        self.goal_time = goal_time
        self.start_time = pygame.time.get_ticks()
        self.current_time = 0
        self.flagged = False

    def reset(self):
        self.start_time = pygame.time.get_ticks()
        self.current_time = 0


# def timer(self):
#         self.time_to_release = False
#         new_time = pygame.time.get_ticks()
#         delta_time = (new_time - self.old_time) /1000
#
#         if delta_time >= self.creature_release_time:
#             if self.currently_releasing:
#                 self.time_to_release = True
#                 self.time_lapsed = 0
#             self.old_time = pygame.time.get_ticks()