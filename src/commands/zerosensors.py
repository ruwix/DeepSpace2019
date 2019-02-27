from wpilib.command import InstantCommand

from subsystems import drive, longarm, shortarm
import odemetry


class ZeroSensors(InstantCommand):
    def __init__(self):
        super().__init__()
        self.drive = drive.Drive()
        self.longarm = longarm.LongArm()
        self.shortarm = shortarm.ShortArm()
        self.odemetry = odemetry.Odemetry()
        self.requires(self.drive)
        self.requires(self.longarm)
        self.requires(self.shortarm)

    def initialize(self):
        self.drive.reset()
        self.longarm.reset()
        self.shortarm.reset()
        self.odemetry.reset()
