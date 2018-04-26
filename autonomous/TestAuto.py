from magicbot import AutonomousStateMachine, tunable, timed_state

from components.DriveTrain import DriveTrain
import wpilib
                    
class Test(AutonomousStateMachine):

    MODE_NAME = 'Test'

    def __init__(self):
    
        self.drivetrain = DriveTrain
        self.i2c = wpilib.I2C(wpilib.I2C.Port.kOnboard, 4)       

    @timed_state(duration=5, first=True)
    def sendAndReceiveData(self):
        # Write bytes 'text', and receive 4 bytes in data
        self.i2c.transaction(b'start', 1)
        data = str(self.i2c.read(4, 1))
        print(data)

        # self.i2c.transaction(b'stop', 1)
