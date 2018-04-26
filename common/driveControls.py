'''

 -- Driver Controller System --

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

import threading
import time
import wpilib
import wpilib.drive

class driveControls (threading.Thread):
    
    def __init__(self, name, driveController, drivetrain, joystick, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.driveController = driveController
        self.delay = delay
        self.drivetrain = drivetrain
        self.joystick = joystick

        self.driveSpeed = 0
        self.turnSpeed = 0
        self.summedSpeed = 0

    def run(self):

        while True:

            time.sleep(self.delay)

            #if (self.joystick.getRawAxis(2))
            self.summedSpeed = self.joystick.getRawAxis(2) * -0.7 + self.joystick.getRawAxis(3) * 0.7
            
            if (self.joystick.getX() > 0.1 or self.joystick.getX() < -0.1 or self.summedSpeed > 0.1 or self.summedSpeed < -0.1):
                
                
                if (self.joystick.getX() > 0.1):
                    self.turnSpeed = (self.joystick.getX() * 0.54) * 0.8 + 0.2
                elif (self.joystick.getX() < -0.1):
                    self.turnSpeed = (self.joystick.getX() * 0.5) * 0.8 + -0.2
                else:
                    self.turnSpeed = 0
                    
                if (self.summedSpeed > 0.1):
                    self.driveSpeed = (self.summedSpeed) * 0.8 + 0.2
                elif (self.summedSpeed < -0.1):
                    self.driveSpeed = (self.summedSpeed) * 0.8 + -0.2
                    self.turnSpeed = self.turnSpeed * -1
                else:
                    self.driveSpeed = 0
                
            else:
                self.driveSpeed = 0
                self.turnSpeed = 0
                self.summedSpeed = 0
            
            self.drivetrain.arcadeDrive(self.driveSpeed, self.turnSpeed)
