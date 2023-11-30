import numpy as np
import sys
from constants import *

from pyPS4Controller.controller import Controller
import time

class BBController(Controller):
    """
    This controller class can be implemented in many different ways and this is one of them.
    """
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.MAX_TZ = 0.5 # Nm
        self.MAX_VELOCITY = 0.85 # rad/sec

        self.DELTA_KP = 0.1
        self.DELTA_KD = 0.01

        self.MAX_ROTATION_TIME = 0.75 # Sec
        self.Tz = 0.0

        self.dphi_y_sp = 0.0
        self.dphi_x_sp = 0.0

        self.theta_kp = 9.0
        self.theta_ki = 0.0
        self.theta_kd = 0.1

        self.COOLDOWN = 0.5
        self.MAX_ROTATION_ITER = int(self.MAX_ROTATION_TIME/DT)

    def on_R2_press(self, value):
        self.dphi_y_sp = 1.0 * self.MAX_VELOCITY * (1.0 + value/JOYSTICK_SCALE)/2.0

    def on_R2_release(self):
        # TODO: Release mechanism
        self.dphi_y_sp = 0.0

    def on_L2_press(self, value):
        self.dphi_y_sp = -1.0 * self.MAX_VELOCITY * (1.0 + value/JOYSTICK_SCALE)/2.0

    def on_L2_release(self):
        # TODO: Release mechanism
        self.dphi_y_sp = 0.0

    def on_R1_press(self):
        for i in range(0, self.MAX_ROTATION_ITER):
            self.Tz = self.MAX_TZ * np.sin(i)
            time.sleep(DT)

        time.sleep(self.COOLDOWN)
    
    def on_R1_release(self):
        self.Tz = 0.0

    def on_L1_press(self):
        for i in range(0, self.MAX_ROTATION_ITER):
            self.Tz = -1.0 * self.MAX_TZ * np.sin(i)
            time.sleep(DT)

        time.sleep(self.COOLDOWN)
    
    def on_L1_release(self):
        self.Tz = 0.0

    def on_triangle_press(self):
        self.theta_kp += self.DELTA_KP

        if self.theta_kp > MAX_THETA_KP:
            self.theta_kp = MAX_THETA_KP
            print("Maxed out Theta Kp at {:.2f}.".format(self.theta_kp))
        else:
            print("Increased Theta Kp to {:.2f}.".format(self.theta_kp))

    def on_triangle_release(self):
        pass

    def on_x_press(self):
        self.theta_kp -= self.DELTA_KP

        if self.theta_kp < MIN_THETA_KP:
            self.theta_kp = MIN_THETA_KP
            print("Bottomed out Theta Kp at {:.2f}.".format(self.theta_kp))
        else:
            print("Decreased Theta Kp to {:.2f}".format(self.theta_kp))

    def on_x_release(self):
        pass

    def on_circle_press(self):
        self.theta_kd += self.DELTA_KD
        if self.theta_kd > MAX_THETA_KD:
            self.theta_kd = MAX_THETA_KD
            print("Maxed out Theta Kd at {:.2f}.".format(self.theta_kd))
        else:        
            print("Increased Theta Kd to {:.2f}.".format(self.theta_kd))

    def on_circle_release(self):
        pass

    def on_square_press(self):
        self.theta_kd -= self.DELTA_KD
        if self.theta_kd < MIN_THETA_KD:
            self.theta_kd = MIN_THETA_KD
            print("Bottomed out Theta Kd at {:.2f}.".format(self.theta_kd))
        else:        
            print("Decreased Theta Kd to {:.2f}".format(self.theta_kd))

    def on_square_release(self):
        pass

    def on_options_press(self):
        print("Exiting controller thread.")
        sys.exit()
