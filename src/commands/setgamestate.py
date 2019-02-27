from wpilib.command import CommandGroup

from subsystems import intake
from utils.gamestate import GameState
from commands import setshortarm, setlongarm, tankarm
from constants import Constants
from wpilib import SmartDashboard as Dash
import logging


class SetGameState(CommandGroup):
    def __init__(self, state):
        super().__init__()
        self.state = state
        posture = Constants.GAME_STATES[self.state.value]
        self.addParallel(setshortarm.SetShortArm(posture[0]))
        self.addParallel(setlongarm.SetLongArm(posture[2]))

    def initialize(self):
        pass

    def end(self):
        pass
