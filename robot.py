#!/usr/bin/env python3

'''
    Blue Crew Robot Code for FIRST Power Up
    Codename: Kylo
'''

import wpilib
import wpilib.drive
import threading

from wpilib.buttons import JoystickButton
from magicbot import MagicRobot
from robotpy_ext.common_drivers import navx

from components.DriveTrain import DriveTrain
from common.driveControls import driveControls
from common.subsystemAux import subsystemAux
from common.driveAux import driveAux

from common.xbox import XboxController

class Kylo(MagicRobot):
    
    # Initialize Robot Components
    drivetrain = DriveTrain

    def createObjects(self):

        # Define Driving Motors
        self.rightDrive = wpilib.VictorSP(0)
        self.leftDrive = wpilib.VictorSP(1)

        # Create Robot Drive
        self.robotDrive = wpilib.drive.DifferentialDrive(self.rightDrive, self.leftDrive)

        # Create Shifter Pneumatics
        self.shifterSolenoid = wpilib.DoubleSolenoid(0, 0, 1)

        # Joysticks and Controllers
        self.driveJoystick = wpilib.Joystick(0)
        self.driveController = XboxController(0)
        
        self.subsystemJoystick = wpilib.Joystick(1)
        self.subsystemController = XboxController(1)

        # Create NavX and Accel
        self.navX = navx.AHRS.create_spi()
        self.accel = wpilib.BuiltInAccelerometer()

        # Set Drivespeed
        self.driveSpeed = 0

       # Create Cube Intake Pneumatics
        self.intakeSolenoid = wpilib.Solenoid(0, 2)

        # Create Timer (For Making Timed Events)
        self.timer = wpilib.Timer()

        # Initialize Compressor
        self.compressor = wpilib.Compressor()

        # Create CameraServer
        wpilib.CameraServer.launch("common/multipleCameras.py:main")

        # Set Gear in Dashboard
        wpilib.SmartDashboard.putString("Shift State", "Low Gear")

    def teleopInit(self):

        # Init Drive Controls
        DriverController = driveControls("DriveController", self.driveController, self.drivetrain, self.driveJoystick, .05)
        DriveAux = driveAux("DriveAux", self.driveController, self.drivetrain, self.driveJoystick, .05)

        SubsystemAux = subsystemAux("SubsystemAux", self.subsystemController, self.driveJoystick, .1)
       
        # Start Drive Controls
        DriveAux.start()
        DriverController.start()

        # Start Subsystem Controls
        SubsystemAux.start()
        
        # Start and Reset Timer
        self.timer.reset()
        self.timer.start()

    def teleopPeriodic(self):

        # Pressurize Throughout Teleop
        self.compressor.start()

        # Rumble Controller
        if (self.timer.get() > 75 and self.timer.get() < 105):
            self.driveController.rumble(1, 1)
        else:
            self.driveController.rumble(0, 0)

if __name__ == '__main__':
    wpilib.run(Kylo)
