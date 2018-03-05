'''

 -- Arm Mech --

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

import threading
import time
import wpilib
import wpilib.drive

class armMech (threading.Thread):

    def __init__(self, name, controller, joystick, cube, ramp, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.subsystemController = controller
        self.delay = delay
        self.cubemech = cube
        self.ramp = ramp

    def run(self):
        while True:
            
            time.sleep(self.delay)

            if (self.subsystemController.right_trigger()):
                self.cubemech.liftArm()
                print("RIGHT TRIGGER")
            elif (self.subsystemController.left_trigger()):
                self.cubemech.lowerArm()
                print("LEFT TRIGGER")
            else:
                self.cubemech.stop()
