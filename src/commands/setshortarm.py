from wpilib.command import Command, InstantCommand
from subsystems import shortarm
from constants import Constants
import math


class SetShortArm(InstantCommand):
    def __init__(self, setpoint):
        super().__init__()
        self.arm = shortarm.ShortArm()
        self.requires(self.arm)
        self.setpoint = setpoint

    def initialize(self):
        self.arm.setAngle(self.setpoint)

    def end(self):
        pass
