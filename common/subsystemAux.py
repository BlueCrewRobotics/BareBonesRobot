'''

 -- Subsystem Aux --

Blue Crew Robotics Team 6153
Authors: Jacob Mealey, Matthew Gallant

'''

import threading
import time
import wpilib
import wpilib.drive

class subsystemAux (threading.Thread):
    def __init__(self, name, controller, joystick, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.subsystemController = controller
        self.delay = delay

    def run(self):
        while True:
            
            time.sleep(self.delay)

            if (self.subsystemController.a() and self.subsystemController.y()):
                print("Deploy Ramps")
                time.sleep(0.5)
            elif (self.subsystemController.a() and self.subsystemController.x()):
                print("Raise Right Ramp")
            elif (self.subsystemController.a() and self.subsystemController.b()):
                print("Lower Right Ramp")
            elif (self.subsystemController.b()):
                print("Clamp Cube")
                
            else:
                print("Nothing To Do")
