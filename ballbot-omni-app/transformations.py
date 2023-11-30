"""
Transformation methods for the ROB311 ballbot.

Author: Senthur Ayyappan, Japmanjeet Singh Gill, and Elliott Rouse
Neurobionics Lab / Locomotor Control Lab
"""

def transform_w2b(m1, m2, m3):
    """
    Transforms the given motor attributes to ball attributes.

    Parameters:
    ----------
    m1: Motor 1's attribute
    m2: Motor 2's attribute
    m3: Motor 3's attribute

    Returns:
    --------
    x: Ball's attribute along x-axis
    y: Ball's attribute along y-axis
    z: Ball's attribute along z-axis
    """

    # Kinematic Transformation
    x = 0.323899 * m2 - 0.323899 * m3
    y = -0.374007 * m1 + 0.187003 * m2 + 0.187003 * m3
    z = 0.187003 * m1 + 0.187003 * m2 + 0.187003 * m3

    return x, y, z

def transform_b2w(bx, by, bz):
    """
    Transforms the given ball attributes to motor attributes.

    Parameters:
    ----------
    bx: Ball's attribute along x-axis
    by: Ball's attribute along y-axis
    bz: Ball's attribute along z-axis

    Returns:
    --------
    m1: Motor 1's attribute
    m2: Motor 2's attribute
    m3: Motor 3's attribute
    """

    # Kinematic Transformation
    m1 = 1.7825 * bz - 1.7825 * by
    m2 = 1.5437 * bx + 0.8912 * by + 1.7825 * bz
    m3 = 0.8912 * by - 1.5437 * bx + 1.7825 * bz

    return m1, m2, m3

def compute_motor_torques(Tx, Ty, Tz):
    '''
    Computes the motor torques based on the given external torques.

    Parameters:
    ----------
    Tx: Torque along x-axis
    Ty: Torque along y-axis
    Tz: Torque along z-axis

    Returns:
    --------
    T1: Motor Torque 1
    T2: Motor Torque 2
    T3: Motor Torque 3

    Motor Torque Diagram:
            Ty
            T1
            |
            |
            |
            . _ _ _ _ Tx
           / \
          /   \
         /     \
        /       \
       T2       T3
    '''

    # Torque Transformation
    T1 = (-0.3333) * (Tz - (2.8284 * Ty))
    T2 = (-0.3333) * (Tz + (1.4142 * (Ty + 1.7320 * Tx)))
    T3 = (-0.3333) * (Tz + (1.4142 * (Ty - 1.7320 * Tx)))

    return T1, T2, T3