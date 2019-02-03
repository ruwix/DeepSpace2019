from wpilib import SmartDashboard as Dash
from wpilib.command import Subsystem

from constants import Constants
from utils import singleton, units, lazytalonsrx


class FrontArm(Subsystem, metaclass=singleton.Singleton):
    """The front arm subsystem controls the front arm motors and encoders."""

    def __init__(self):
        super().__init__()

    def init(self):
        """Initialize the front arm motors. This is not in the constructor to make the calling explicit in the robotInit to the robot simulator."""
        self.s_motor = lazytalonsrx.LazyTalonSRX(Constants.FS_MOTOR_ID)
        self.m_motor = lazytalonsrx.LazyTalonSRX(Constants.FM_MOTOR_ID)
        self.s_motor.initialize(
            inverted=False, encoder=True, name="Front Arm Slave")
        self.m_motor.initialize(
            inverted=False, encoder=True, name="Front Arm Master")
        self.s_motor.follow(self.m_motor)
        self.m_motor.setPositionPIDF(
            Constants.FRONT_ARM_KP, Constants.FRONT_ARM_KI, Constants.FRONT_ARM_KD, Constants.FRONT_ARM_KF)

    def zeroSensors(self):
        """Set the encoder positions to 0."""
        self.m_motor.zero()

    def outputToDashboard(self):
        self.s_motor.outputToDashboard()
        self.m_motor.outputToDashboard()

    def getAngle(self):
        """Get the angle of the arm in degrees."""
        self.m_motor.getPosition()

    def setAngle(self, angle):
        """Set the angle of the arm in degrees."""
        self.m_motor.setPositionSetpoint(angle)

    def periodic(self):
        self.outputToDashboard()
