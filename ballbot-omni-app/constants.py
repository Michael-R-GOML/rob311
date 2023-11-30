import numpy as np

# Maximum value returned by the joystick thumbsticks
JOYSTICK_SCALE = 32767

# Frequency of the main control loop, defaults to 200Hz
FREQ = 200
DT = 1 / FREQ

# Ballbot Parameters
RW = 0.048  # Wheel radius
RK = 0.1210  # Distance from wheel center to robot center
ALPHA = np.deg2rad(45)  # Angle between wheel and robot center
MK = 0.62369  # Wheel mass
IK = 0.00365  # Wheel moment of inertia

# Filter Parameters
# Lowpass Filter Parameters
Fs = FREQ  # Sampling rate in Hz
Fc = 0.8  # Cut-off frequency of the filter in Hz
Fn = Fc / Fs  # Normalized equivalent of Fc
N = 100  # Taps of the filter

# Weighted Moving Average Parameters
WMA_WEIGHTS = np.array([20, 40, 60, 80])  # Weight values for moving average
WMA_WINDOW_SIZE = len(WMA_WEIGHTS)  # Window size for moving average
WMA_NORM = WMA_WEIGHTS / np.sum(WMA_WEIGHTS)  # Normalized weights for moving average

# Maximum Lean Angle
MAX_THETA = np.deg2rad(4)  # Maximum lean angle: 4 degrees

# Maximum Duty Cycles (Maybe limiting their ratio would be better?)
MAX_STA_DUTY = 0.6  # Maximum duty cycle for steering actuator
MAX_VEL_DUTY = 0.4  # Maximum duty cycle for velocity actuator

MAX_DPHI = 4.0  # Maximum angular velocity
MAX_DDPHI = 40.0  # Maximum angular acceleration

# Deadband for Ball Velocity
DPHI_DEADBAND = 0.5  # Deadband for Ball velocity

# Stability Controller Gains
ROLL_THETA_KP = 0.0  # Roll angle proportional gain
ROLL_THETA_KI = 0.0  # Roll angle integral gain
ROLL_THETA_KD = 0.0  # Roll angle derivative gain

PITCH_THETA_KP = 0.0  # Pitch angle proportional gain
PITCH_THETA_KI = 0.0  # Pitch angle integral gain
PITCH_THETA_KD = 0.0  # Pitch angle derivative gain

# Steering Controller Gains (Can be either a velocity or a position controller)
DPHI_KP = 0.0  # Lean angle proportional gain
DPHI_KI = 0.0  # Lean angle integral gain
DPHI_KD = 0.0  # Lean angle derivative gain

# Theta Kp Range for tuning the stability controller on the fly with the ps4 controller.
MAX_THETA_KP = 20.0  # Maximum theta Kp value
MIN_THETA_KP = 2.0  # Minimum theta Kp value

# Theta Kd Range for tuning the stability controller on the fly with the ps4 controller.
MAX_THETA_KD = 6.0  # Maximum theta Kd value
MIN_THETA_KD = -6.0  # Minimum theta Kd value