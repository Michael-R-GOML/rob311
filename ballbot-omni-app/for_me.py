         # LAB 9
        # Compute ball rotation (phi) with psi_1, psi_2, and psi_3
        def compute_phi(psi_1, psi_2, psi_3)
            Rw = .0478 # meters
            Rk = .11925 # meters
            
            dw1 = [-1 0 0]
            dw2 = [1/2 -sqrt(3)/2 0]
            dw3 = [1/2 sqrt(3)/2 0]



        return phi_x, phi_y, phi_z

        phi_x, phi_y, phi_z = compute_phi(psi_1, psi_2, psi_3)
        # print("PHI X: {}, PHI Y: {}, PHI Z: {}".format(phi_x, phi_y, phi_z))
        # ---------------------------------------------

        # ---------------------------------------------
        # LAB 9
        # Construct the data matrix for saving - you can add more variables by replicating the format below
        # Append the following variables to the data variable:
        # motor torques - T1, T2, T3
        # ball rotations - phi_x, phi_y, phi_z
        # wheel rotations - psi_1, psi_2, psi_3

        data = [i, t_now, theta_x, theta_y, phi_x, phi_y, phi_z, psi_1, psi_2, psi_3, T1, T2, T3]