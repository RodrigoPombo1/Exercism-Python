from random import randint
import random

class Robot:
    names = []
    
    def __init__(self):
        while True:
            random.seed()
            try_name = chr(randint(0, 26) + ord("A")) + chr(randint(0, 26) + ord("A")) + str(randint(0, 10)) + str(randint(0, 10)) + str(randint(0, 10))
            if try_name not in Robot.names:
                self.name = try_name
                Robot.names.append(self.name)
                break

    def reset(self):
        Robot.names.remove(self.name)
        self.__init__()
